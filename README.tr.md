# TM Neural HUD Video Studio (`TM-neural-hud-video-studio`)

<div align="center">

**Deterministic Cyberpunk HUD Telemetry & Video Engine for AI Repositories**  
**Yapay Zeka Depoları ve Ajan Mimarileri İçin Deterministik Siberpunk HUD Telemetri Video Motoru**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium%20Headless-45ba4b.svg)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20%2B%20AAC-007808.svg)](https://ffmpeg.org)
[![Author](https://img.shields.io/badge/Author-Taqi%20Molavi-orange.svg)](https://molavi.pro)
[![Agency](https://img.shields.io/badge/Agency-Inten%20Asia-red.svg)](https://inten.asia)

**[English](README.md) | [فارسی](README.fa.md) | [Türkçe](README.tr.md) | [Azərbaycan](README.az.md) | [العربية](README.ar.md)**

<br/>

[![TM Neural HUD Video Studio Demosu](https://molavi.pro/videos/neural-hud/neural-hud-studio-poster.jpg)](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)

*Yüksek Çözünürlüklü Siberpunk HUD Telemetri Videosu — [molavi.pro Üzerinde Doğrudan İzleyin](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)*

</div>

---

## 1. Genel Bakış

**TM Neural HUD Video Studio**, karmaşık yazılım depolarını, mikroservisleri ve otonom yapay zeka ajan iş akışlarını fütüristik siberpunk HUD telemetri tanıtım videolarına dönüştüren otonom bir mühendislik motorudur.

Matematiksel olarak deterministik zaman ilerleme döngüsü (`window.seekTo(t)`) sayesinde, her kare başsız Chromium (Playwright) üzerinden tam piksel hassasiyetiyle yakalanır ve algoritmik siber sub-bass sesleriyle birlikte doğrudan FFmpeg kodlayıcısına aktarılır.

### Temel Özellikler:
- **Deterministik Kare İşleme:** Kare atlama ve gecikme olmaksızın, matematiksel `t = frame_index / fps` bağıntısıyla tam kare senkronizasyonu.
- **Hafif Git Boyutu:** Ağır video dosyaları doğrudan [molavi.pro CDN](https://molavi.pro/videos/neural-hud/) sunucularında barındırılır; GitHub geçmişi temiz ve hafif kalır.
- **Harici Örnek İstemeyen Ses:** Veri merkezi uğultuları, radyo telemetri sinyalleri ve nabız efektleri tamamen FFmpeg filtreleriyle algoritmik olarak üretilir.
- **Çoklu Ekran Oranları:** Mobil dikey format (`9:16`) ve masaüstü yatay format (`16:9`) desteği.

---

## 2. Mimari ve Boru Hattı

```
┌────────────────────────────────────────────────────────┐
│             HTML5 / Canvas HUD Kontrol Paneli          │
│  - 3B Sinir Ağı Parçacık Küresi (Fibonacci Dağılımı)   │
│  - Holografik İzole Alt Sistem & Dönen Radar Ekranı    │
│  - 3 Gerçek Zamanlı Modül Durum ve Sağlık Kartı        │
│  - 3 Sütunlu Alt Telemetri Şeridi:                     │
│    [1] Yönlendirme ve Loglar + Dalga Veri Grafiği      │
│    [2] İş Parçacığı / İzleme + Gecikme & Önbellek      │
│    [3] Canlı AST Kod Farkı / Canlı Değişiklik Akışı    │
└──────────────────────────┬─────────────────────────────┘
                           │ window.seekTo(t)
             ┌─────────────┴─────────────┐
             ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐
 │ Başsız Playwright     │   │  FFmpeg Algoritmik    │
 │ Kare Çerçeve Akışı    │   │  Siber Ses Sentezci   │
 └───────────┬───────────┘   └───────────┬───────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
          [ Yayın Formatı Konteyner (H.264 / AAC) ]
                           │
                           ▼
          [ molavi.pro CDN Üzerinde Barındırma ]
```

---

## 3. Ekosistem Hazır Ayarları ve Örnekler

| Depo | Odak ve Alan | Video Bağlantısı | Örnek Yapılandırma |
| :--- | :--- | :--- | :--- |
| **[MWIE](https://github.com/tmolavi/molavi-web-intelligence)** | Molavi Web İstihbarat Motoru (SEO & AEO) | [Videoyu İzle](https://molavi.pro/videos/neural-hud/mwie-hud.mp4) | [`examples/mwie/`](examples/mwie/) |
| **[SAGE Audit](https://github.com/tmolavi/sage-audit)** | Üç Sütunlu Teknik SEO, AEO ve GEO Denetimi | [Videoyu İzle](https://molavi.pro/videos/neural-hud/sage-audit-hud.mp4) | [`examples/sage-audit/`](examples/sage-audit/) |
| **[GEO-Scope](https://github.com/tmolavi/geo-scope)** | Yapay Zeka Arama Motoru Alıntı Ölçümü | [Videoyu İzle](https://molavi.pro/videos/neural-hud/geo-scope-hud.mp4) | [`examples/geo-scope/`](examples/geo-scope/) |
| **[TM Second Brain](https://github.com/tmolavi/tm-second-brain)** | SQLite Tabanlı Kalıcı Çevrimdışı Bellek | [Videoyu İzle](https://molavi.pro/videos/neural-hud/second-brain-hud.mp4) | [`examples/tm-second-brain/`](examples/tm-second-brain/) |

---

## 4. Hızlı Başlangıç

### Kurulum
```bash
git clone https://github.com/tmolavi/TM-neural-hud-video-studio.git
cd TM-neural-hud-video-studio
pip install -e .
playwright install chromium
```

### Komut Satırından Video Üretimi
```bash
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

---

## 5. İlgili Bağlantılar ve Kaynaklar

- Portföy ve Makaleler: [molavi.pro](https://molavi.pro)
- İnceleme Notu: [molavi.pro/tr/notes/tm-neural-hud-video-studio](https://molavi.pro/tr/notes/tm-neural-hud-video-studio)
- Dijital Pazarlama: [Inten Asia](https://inten.asia)
- Beceriler Dizini: [MCP Agent Skills Hub](https://github.com/tmolavi/mcp-agent-skills-hub)

---

## 6. Lisans

[MIT Lisansı](LICENSE) altında yayımlanmıştır.  
Telif Hakkı (c) 2026 **Taghi Molavi** ([molavi.pro](https://molavi.pro)).
