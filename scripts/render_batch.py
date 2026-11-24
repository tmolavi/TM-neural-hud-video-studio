#!/usr/bin/env python3
import asyncio
import subprocess
from pathlib import Path
import sys

sys.path.append("/home/taqi/.gemini/config/skills/neural-hud-video-studio/scripts")
from render_video import render_video

TARGETS = [
    ("neural-hud-video-studio", "neural-hud-studio.mp4", "9:16"),
    ("mwie", "mwie-hud.mp4", "9:16"),
    ("sage-audit", "sage-audit-hud.mp4", "9:16"),
    ("geo-scope", "geo-scope-hud.mp4", "9:16"),
    ("tm-second-brain", "second-brain-hud.mp4", "9:16"),
]

OUT_DIR = Path("/Users/taghimolavi/Downloads/git/molavi.pro/public/videos/neural-hud")
OUT_DIR.mkdir(parents=True, exist_ok=True)

async def main():
    print("==================================================================")
    print(" Starting Neural HUD Video Batch Rendering & Hosting Pipeline")
    print("==================================================================")
    
    for slug, filename, aspect in TARGETS:
        out_path = OUT_DIR / filename
        print(f"\n>>> Rendering {slug} -> {out_path} ({aspect}, 6.0s, 24fps)...")
        await render_video(
            repo_slug=slug,
            output_path=str(out_path),
            aspect=aspect,
            duration=6.0,
            fps=24
        )
        
        # Extract crisp poster snapshot at t=1.5s
        poster_path = OUT_DIR / filename.replace(".mp4", "-poster.jpg")
        cmd_poster = [
            "ffmpeg", "-y",
            "-ss", "00:00:01.5",
            "-i", str(out_path),
            "-vframes", "1",
            "-q:v", "2",
            str(poster_path)
        ]
        subprocess.run(cmd_poster, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✓ Snapshot poster generated: {poster_path}")

    print("\n==================================================================")
    print(" All HUD videos rendered and hosted successfully in molavi.pro!")
    print("==================================================================")

if __name__ == "__main__":
    asyncio.run(main())
