# TM Neural HUD Video Studio (`TM-neural-hud-video-studio`)

<div align="center">

**Deterministic Cyberpunk HUD Telemetry & Video Engine for AI Repositories**  
**Süni İntellekt Repozitoriyaları və Agent Arxitekturaları üçün Deterministik Kiberpank HUD Telemetriya Video Mühərriki**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium%20Headless-45ba4b.svg)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20%2B%20AAC-007808.svg)](https://ffmpeg.org)
[![Author](https://img.shields.io/badge/Author-Taqi%20Molavi-orange.svg)](https://molavi.pro)
[![Agency](https://img.shields.io/badge/Agency-Inten%20Asia-red.svg)](https://inten.asia)

**[English](README.md) | [فارسی](README.fa.md) | [Türkçe](README.tr.md) | [Azərbaycan](README.az.md) | [العربية](README.ar.md)**

<br/>

[![TM Neural HUD Video Studio Nümayişi](https://molavi.pro/videos/neural-hud/neural-hud-studio-poster.jpg)](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)

*Yüksək Dəqiqlikli Kiberpank HUD Telemetriya Videosu — [molavi.pro Üzərində Birbaşa İzləyin](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)*

</div>

---

## 1. Layihənin İcmalı

**TM Neural HUD Video Studio**, proqram təminatı repozitoriyalarını, mikroxidmətləri və avtonom süni intellekt agentlərinin mürəkkəb arxitekturalarını yüksək səviyyəli kiberpank HUD telemetriya təqdimat videolarına çevirən mühəndislik mühərrikidir.

Riyazi olaraq deterministik zaman idarəetməsi (`window.seekTo(t)`) sayəsində hər bir kadr başsız Chromium (Playwright) vasitəsilə tam piksel dəqiqliyi ilə çəkilir və alqoritmik siber sub-bas və radar səsləri ilə birlikdə birbaşa FFmpeg kodlayıcısına ötürülür.

### Əsas Üstünlüklər:
- **Deterministik Kadr Çıxarışı:** Kadr itkisi olmadan, dəqiq riyazi `t = frame_index / fps` düsturu ilə hər bir saniyənin dəqiq vizuallaşdırılması.
- **Yüngül Git Həcmi:** Ağır video faylları birbaşa [molavi.pro CDN](https://molavi.pro/videos/neural-hud/) serverlərində yerləşdirilir; GitHub repozitoriyası yüngül və sürətli qalır.
- **Sintez Olunmuş Kibersəs:** Data mərkəzi səsləri, telemetriya siqnalları və nəbz effektləri heç bir xarici səs faylı olmadan birbaşa FFmpeg daxilində generasiya edilir.
- **Çoxformatlı Dəstək:** Mobil şaquli format (`9:16`) və masaüstü üfüqi format (`16:9`) dəstəyi.

---

## 2. Arxitektura və Məlumat Xətti

```
┌────────────────────────────────────────────────────────┐
│             HTML5 / Canvas HUD Nəzarət Paneli          │
│  - 3D Neyron Şəbəkə Hissəcik Kürəsi (Fibonaççi Şəbəkəsi)│
│  - Huloqrafik İzolyasiya Alt Sistemi və Radar Ekranı   │
│  - 3 Real Zamanlı Modul Vəziyyəti Kartı                │
│  - 3 Sütunlu Alt Telemetriya Zolağı:                   │
│    [1] Marşrutlaşdırma və Loqlar + Dalğa Qrafiki       │
│    [2] Axın / İzləmə + Gecikmə və Keş Göstəriciləri     │
│    [3] Canlı AST Kod Dəyişikliyi / Canlı Dif Axını     │
└──────────────────────────┬─────────────────────────────┘
                           │ window.seekTo(t)
             ┌─────────────┴─────────────┐
             ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐
 │ Başsız Playwright     │   │  FFmpeg Alqoritmik    │
 │ Kadr Axını            │   │  Kibersəs Sintezatoru │
 └───────────┬───────────┘   └───────────┬───────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
          [ Yayım Formatlı Konteyner (H.264 / AAC) ]
                           │
                           ▼
          [ molavi.pro CDN Üzərində Yerləşdirmə ]
```

---

## 3. Ekosistem Hazır Tənzimləmələri və Nümunələr

| Repozitoriya | İstiqamət və Sahə | Video Keçidi | Nümunə Qovluğu |
| :--- | :--- | :--- | :--- |
| **[MWIE](https://github.com/tmolavi/molavi-web-intelligence)** | Molavi Veb Kəşfiyyat Mühərriki (SEO & AEO) | [Videoya Bax](https://molavi.pro/videos/neural-hud/mwie-hud.mp4) | [`examples/mwie/`](examples/mwie/) |
| **[SAGE Audit](https://github.com/tmolavi/sage-audit)** | Üç Sütunlu Texniki SEO, AEO və GEO Auditi | [Videoya Bax](https://molavi.pro/videos/neural-hud/sage-audit-hud.mp4) | [`examples/sage-audit/`](examples/sage-audit/) |
| **[GEO-Scope](https://github.com/tmolavi/geo-scope)** | Süni İntellekt Axtarış İstinad Meyarı | [Videoya Bax](https://molavi.pro/videos/neural-hud/geo-scope-hud.mp4) | [`examples/geo-scope/`](examples/geo-scope/) |
| **[TM Second Brain](https://github.com/tmolavi/tm-second-brain)** | SQLite Əsaslı Daimi Oflayn Yaddaş | [Videoya Bax](https://molavi.pro/videos/neural-hud/second-brain-hud.mp4) | [`examples/tm-second-brain/`](examples/tm-second-brain/) |

---

## 4. Sürətli Başlanğıc

### Quraşdırma
```bash
git clone https://github.com/tmolavi/TM-neural-hud-video-studio.git
cd TM-neural-hud-video-studio
pip install -e .
playwright install chromium
```

### Video Render Əmri
```bash
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

---

## 5. Əlaqəli Keçidlər və Resurslar

- Portfolio və Məqalələr: [molavi.pro](https://molavi.pro)
- İcmal Məqaləsi: [molavi.pro/az/notes/tm-neural-hud-video-studio](https://molavi.pro/az/notes/tm-neural-hud-video-studio)
- Rəqəmsal Marketinq: [Inten Asia](https://inten.asia)
- Bacarıqlar Kataloqu: [MCP Agent Skills Hub](https://github.com/tmolavi/mcp-agent-skills-hub)

---

## 6. Lisenziya

[MIT Lisenziyası](LICENSE) altında buraxılmışdır.  
Müəlliflik Hüququ (c) 2026 **Tağı Mövləvi** ([molavi.pro](https://molavi.pro)).
