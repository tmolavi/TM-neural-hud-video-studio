#!/usr/bin/env python3
import asyncio
import subprocess
import tempfile
from pathlib import Path
from playwright.async_api import async_playwright

DURATION = 12.0
FPS = 24
WIDTH = 720
HEIGHT = 1280

OUT_MP4 = Path("/Users/taghimolavi/Downloads/git/molavi.pro/public/videos/neural-hud/neural-hud-studio-hd.mp4")
OUT_POSTER = Path("/Users/taghimolavi/Downloads/git/molavi.pro/public/videos/neural-hud/neural-hud-studio-hd-poster.jpg")
TEMPLATE = Path("/home/taqi/.gemini/config/skills/neural-hud-video-studio/templates/showcase_highlevel.html.tmpl")

def generate_cinematic_audio(duration: float, out_aac: str):
    fade_out = duration - 1.5
    filter_complex = (
        f"aevalsrc=exprs='0.34*sin(2*PI*55*t)+0.16*sin(2*PI*82.41*t)+0.10*sin(2*PI*110*t)*sin(2*PI*0.5*t)':s=44100:d={duration}[sub];"
        f"anoisesrc=d={duration}:c=pink:r=44100,lowpass=f=320,volume=0.28[pad];"
        f"aevalsrc=exprs='0.22*sin(2*PI*1046.5*t)*gt(mod(t,3.0),2.92)+0.15*sin(2*PI*1567.98*t)*gt(mod(t,1.5),1.46)':s=44100:d={duration}[pings];"
        f"aevalsrc=exprs='0.10*sin(2*PI*(330+220*sin(2*PI*0.25*t))*t)':s=44100:d={duration}[sweep];"
        f"[sub][pad][pings][sweep]amix=inputs=4:duration=first,"
        f"afade=t=in:ss=0:d=0.6,afade=t=out:st={fade_out}:d=1.5[out]"
    )
    cmd = [
        "ffmpeg", "-y", "-filter_complex", filter_complex,
        "-map", "[out]", "-t", str(duration),
        "-ac", "2", "-c:a", "aac", "-b:a", "192k", out_aac
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Audio synth failed: {res.stderr}")

async def main():
    OUT_MP4.parent.mkdir(parents=True, exist_ok=True)
    total_frames = int(DURATION * FPS)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_html = Path(tmpdir) / "showcase.html"
        tmp_html.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
        tmp_audio = Path(tmpdir) / "audio.aac"
        tmp_video = Path(tmpdir) / "video_raw.mp4"

        print("[1/4] Synthesizing 12.0s cinematic cyber-telemetry audio...", flush=True)
        generate_cinematic_audio(DURATION, str(tmp_audio))

        ffmpeg_cmd = [
            "ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "mjpeg", "-r", str(FPS),
            "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-preset", "fast", "-crf", "17", str(tmp_video)
        ]
        ff_proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        print(f"[2/4] Capturing {total_frames} HD frames ({WIDTH}x{HEIGHT} @ {FPS}fps via fast MJPEG pipe)...", flush=True)
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-web-security", "--allow-file-access-from-files", "--no-sandbox"]
            )
            page = await browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=1)
            await page.goto(f"file://{tmp_html}")
            await page.wait_for_function("typeof window.seekTo === 'function'")
            await page.evaluate("document.fonts.ready")

            for i in range(total_frames):
                t = i / FPS
                await page.evaluate(f"window.seekTo({t})")
                jpg_bytes = await page.screenshot(type="jpeg", quality=92, timeout=30000, animations="disabled")
                ff_proc.stdin.write(jpg_bytes)
                if (i + 1) % 72 == 0:
                    print(f"   Progress: {i+1}/{total_frames} frames...", flush=True)

            ff_proc.stdin.close()
            ff_proc.wait()
            await browser.close()

        if ff_proc.returncode != 0:
            raise RuntimeError(ff_proc.stderr.read().decode())

        print("[3/4] Muxing HD H.264 + Stereo AAC container...", flush=True)
        mux_res = subprocess.run([
            "ffmpeg", "-y", "-i", str(tmp_video), "-i", str(tmp_audio),
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(OUT_MP4)
        ], capture_output=True, text=True)
        if mux_res.returncode != 0:
            raise RuntimeError(mux_res.stderr)

        subprocess.run([
            "ffmpeg", "-y", "-ss", "00:00:04.0", "-i", str(OUT_MP4),
            "-vframes", "1", "-q:v", "2", str(OUT_POSTER)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("[4/4] Verifying with ffprobe...", flush=True)
        probe = subprocess.run([
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration,size:stream=width,height,codec_name,codec_type",
            "-of", "json", str(OUT_MP4)
        ], capture_output=True, text=True)
        print(probe.stdout, flush=True)

if __name__ == "__main__":
    asyncio.run(main())
