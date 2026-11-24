# TM Neural HUD Video Studio (`TM-neural-hud-video-studio`)

<div align="center">

**Deterministic Cyberpunk HUD Telemetry & Video Engine for AI Repositories**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium%20Headless-45ba4b.svg)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20%2B%20AAC-007808.svg)](https://ffmpeg.org)
[![Author](https://img.shields.io/badge/Author-Taqi%20Molavi-orange.svg)](https://molavi.pro)
[![Agency](https://img.shields.io/badge/Agency-Inten%20Asia-red.svg)](https://inten.asia)

**[English](README.md) | [فارسی](README.fa.md) | [Türkçe](README.tr.md) | [Azərbaycan](README.az.md) | [العربية](README.ar.md)**

<br/>

[![TM Neural HUD Video Studio Demo](https://molavi.pro/videos/neural-hud/neural-hud-studio-poster.jpg)](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)

*High-Tech Cyberpunk HUD Telemetry Video — [Watch High-Res MP4 Stream on molavi.pro](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)*

</div>

---

## 1. Overview

**TM Neural HUD Video Studio** transforms software repositories, microservices, and agent architectures into high-tech cyberpunk HUD telemetry showcase videos.

By implementing a deterministic time-seek pipeline (`window.seekTo(t)`), frames are captured with pixel precision via headless Chromium (Playwright) and encoded directly into FFmpeg alongside algorithmically synthesized cybernetic sub-bass and radar telemetry audio.

### Key Capabilities
- **Mathematical Frame Determinism**: Zero dropped frames through exact mathematical time sampling (`t = frame_index / fps`).
- **Clean Repository Footprint**: Video outputs are hosted on the [molavi.pro CDN](https://molavi.pro/videos/neural-hud/), keeping GitHub repository history lightweight.
- **Synthesized Audio**: Algorithmic sub-bass drones and telemetry chirps synthesized directly in FFmpeg.
- **Ecosystem Integration**: Pre-configured presets for sibling repositories.

---

## 2. Architecture

```
┌────────────────────────────────────────────────────────┐
│             HTML5 / Canvas HUD Dashboard               │
│  - 3D Neural Particle Mesh Sphere (Fibonacci Grid)    │
│  - Holographic Inset Subsystem Window & Radar Sweep   │
│  - 3 Real-Time Module State & Health Cards             │
│  - 3-Column Bottom Telemetry Strip:                    │
│    [1] ROUTING / LOGS + Dynamic Throughput Sparkline   │
│    [2] THREAD / TRACE + Latency / Cache / Token Matrix │
│    [3] LIVE DIFF / OUTPUT + AST Code Resonance Stream │
└──────────────────────────┬─────────────────────────────┘
                           │ window.seekTo(t)
             ┌─────────────┴─────────────┐
             ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐
 │ Playwright Chromium   │   │  FFmpeg Algorithmic   │
 │ Direct Frame Pipe     │   │  Audio Synthesizer    │
 └───────────┬───────────┘   └───────────┬───────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
          [ Broadcast Container (H.264 / AAC) ]
                           │
                           ▼
         [ Hosted on molavi.pro / CDN Delivery ]
```

---

## 3. Featured Ecosystem Presets

| Repository | Focus & Domain | Video Stream | Spec Folder |
| :--- | :--- | :--- | :--- |
| **[MWIE](https://github.com/tmolavi/molavi-web-intelligence)** | Molavi Web Intelligence Engine | [Watch Video](https://molavi.pro/videos/neural-hud/mwie-hud.mp4) | [`examples/mwie/`](examples/mwie/) |
| **[SAGE Audit](https://github.com/tmolavi/sage-audit)** | Tri-Pillar SEO, AEO & GEO Audit | [Watch Video](https://molavi.pro/videos/neural-hud/sage-audit-hud.mp4) | [`examples/sage-audit/`](examples/sage-audit/) |
| **[GEO-Scope](https://github.com/tmolavi/geo-scope)** | AI Search Engine Visibility Benchmark | [Watch Video](https://molavi.pro/videos/neural-hud/geo-scope-hud.mp4) | [`examples/geo-scope/`](examples/geo-scope/) |
| **[TM Second Brain](https://github.com/tmolavi/tm-second-brain)** | Persistent Offline SQLite Memory Vault | [Watch Video](https://molavi.pro/videos/neural-hud/second-brain-hud.mp4) | [`examples/tm-second-brain/`](examples/tm-second-brain/) |

---

## 4. Quick Start

### Installation
```bash
git clone https://github.com/tmolavi/TM-neural-hud-video-studio.git
cd TM-neural-hud-video-studio
pip install -e .
playwright install chromium
```

### CLI Rendering
```bash
# Render vertical 9:16 HUD video (6.0s @ 24fps)
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

---

## 5. Specifications

- **Container**: MP4 (H.264 / AAC)
- **Audio**: 44.1 kHz, 192 kbps
- **Aspect Ratios**: `9:16` (720x1280) and `16:9` (1280x720)
- **Palette**: Obsidian (`#060608`), Crimson (`#ff2a3c`), Amber (`#ff5533`), Cyan (`#00f0ff`)

---

## 6. Links & Resources

- Portfolio: [molavi.pro](https://molavi.pro)
- Showcase Note: [molavi.pro/notes/tm-neural-hud-video-studio](https://molavi.pro/notes/tm-neural-hud-video-studio)
- Digital Marketing: [Inten Asia](https://inten.asia)
- Skills Hub: [MCP Agent Skills Hub](https://github.com/tmolavi/mcp-agent-skills-hub)

---

## 7. License

MIT License - Copyright (c) 2026 **Taghi Molavi** ([molavi.pro](https://molavi.pro)).
