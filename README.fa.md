<div dir="rtl" align="right">

# استودیو ویدیویی تلمتری هاد نیورال (`TM-neural-hud-video-studio`)

<div align="center" dir="ltr">

**Deterministic Cyberpunk HUD Telemetry & Video Engine for AI Repositories**  
**موتور قطعی تولید ویدیوهای تلمتری سایبرپانک HUD برای مخازن کد و عامل‌های هوش مصنوعی**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium%20Headless-45ba4b.svg)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20%2B%20AAC-007808.svg)](https://ffmpeg.org)
[![Author](https://img.shields.io/badge/Author-Taqi%20Molavi-orange.svg)](https://molavi.pro)
[![Agency](https://img.shields.io/badge/Agency-Inten%20Asia-red.svg)](https://inten.asia)

**[English](README.md) | [فارسی](README.fa.md) | [Türkçe](README.tr.md) | [Azərbaycan](README.az.md) | [العربية](README.ar.md)**

<br/>

[![دموی استودیو تلمتری هاد نیورال](https://molavi.pro/videos/neural-hud/neural-hud-studio-poster.jpg)](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)

*ویدیوی تلمتری مهندسی و سایبرپانک هاد — [مشاهده مستقیم فایل ویدیویی با کیفیت بالا در molavi.pro](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)*

</div>

---

## ۱. معرفی و فلسفه پروژه

**TM Neural HUD Video Studio** یک زیرساخت خودکار مهندسی است که مخازن کد، میکروسرویس‌ها، گراف‌های اجرایی و معماری‌های پیچیده عامل‌های هوش مصنوعی را به **ویدیوهای تلمتری هالیوودی و سایبرپانک (HUD Telemetry)** تبدیل می‌کند.

با بهره‌گیری از پایپ‌لاین پیشروی زمانی قطعی (`window.seekTo(t)`)، فریم‌های تصویری بدون پرش و با دقت پیکسلی در کرومیوم بی‌سر (Playwright) رندر شده و همراه با موسیقی الگوریتمی ساب‌بیس و بوق‌های راداری، مستقیماً وارد انکودر FFmpeg می‌شوند.

### مزایای کلیدی:
* **رندرینگ کاملاً قطعی (Zero Hallucinated Frames):** بدون وابستگی به زمان سیستم؛ هر فریم با فرمول ریاضی `t = frame_index / fps` محاسبه می‌شود.
* **سبک نگه‌داشتن مخزن گیت:** ویدیوهای باکیفیت به جای اشغال حجم در گیت، مستقیماً روی سرور توزیع [molavi.pro CDN](https://molavi.pro/videos/neural-hud/) میزبانی می‌شوند.
* **صداگذاری الگوریتمی بدون سمپل خارجی:** فیلترهای صوتی FFmpeg صدای امبینت دیتاسنتر و فرکانس‌های راداری را بدون هیچ فایل صوتی جانبی می‌سازند.
* **سازگاری کامل با ابعاد عمودی و افقی:** پشتیبانی از نسبت ابعاد `9:16` (مناسب ریلز و شورتز) و `16:9` (مناسب مستندات دسکتاپ).

---

## ۲. دیاگرام معماری خط لوله

```
┌────────────────────────────────────────────────────────┐
│             داشبورد تلمتری بر پایه HTML5 / Canvas      │
│  - کره ذرات شبکه عصبی سه‌بعدی (شبکه فیبوناچی)          │
│  - پنجره هولوگرافیک ایزوله زیرسیستم و رادار چرخان       │
│  - کارت‌های وضعیت بلادرنگ ماژول‌های معماری              │
│  - نوار سه‌ستونه پایینی تلمتری:                         │
│    [1] مسیریابی و لاگ‌ها + اسپارک‌لاین موجی تروپوت       │
│    [2] تریس و تردهای همگام + ماتریس لیتنسی و کش        │
│    [3] استریم زنده دیف کد AST و تغییرات زنده سورس‌کد    │
└──────────────────────────┬─────────────────────────────┘
                           │ window.seekTo(t)
             ┌─────────────┴─────────────┐
             ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐
 │ پایپ‌لاین فریم‌های      │   │  سنتز الگوریتمی       │
 │ بدون‌سر Playwright     │   │  صدا در FFmpeg        │
 └───────────┬───────────┘   └───────────┬───────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
          [ ظرف پخش ویدیویی استاندار (H.264 / AAC) ]
                           │
                           ▼
           [ میزبانی و استریم در CDN molavi.pro ]
```

---

## ۳. پریست‌ها و نمونه‌های اکوسیستم مولوی

| مخزن مرجع | حوزه و کاربرد تخصصی | استریم ویدیو در سرور | پوشه نمونه |
| :--- | :--- | :--- | :--- |
| **[MWIE](https://github.com/tmolavi/molavi-web-intelligence)** | موتور هوشمندی وب مولوی (سئو و هوش مصنوعی) | [تماشای ویدیو](https://molavi.pro/videos/neural-hud/mwie-hud.mp4) | [`examples/mwie/`](examples/mwie/) |
| **[SAGE Audit](https://github.com/tmolavi/sage-audit)** | ممیزی سه‌ستونه سئو فنی، AEO و بازیابی مولد | [تماشای ویدیو](https://molavi.pro/videos/neural-hud/sage-audit-hud.mp4) | [`examples/sage-audit/`](examples/sage-audit/) |
| **[GEO-Scope](https://github.com/tmolavi/geo-scope)** | بنچ‌مارک استنادی موتورهای جستجوی هوش مصنوعی | [تماشای ویدیو](https://molavi.pro/videos/neural-hud/geo-scope-hud.mp4) | [`examples/geo-scope/`](examples/geo-scope/) |
| **[TM Second Brain](https://github.com/tmolavi/tm-second-brain)** | حافظه ماندگار محلی آفلاین با SQLite و بردارها | [تماشای ویدیو](https://molavi.pro/videos/neural-hud/second-brain-hud.mp4) | [`examples/tm-second-brain/`](examples/tm-second-brain/) |

---

## ۴. راهنمای راه‌اندازی سریع

### نصب پیش‌نیازها
```bash
git clone https://github.com/tmolavi/TM-neural-hud-video-studio.git
cd TM-neural-hud-video-studio
pip install -e .
playwright install chromium
```

### رندر ویدیوی سفارشی با خط فرمان
```bash
# رندر ویدیوی عمودی 9:16 برای شبکه‌های اجتماعی (۶ ثانیه با ۲۴ فریم در ثانیه)
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

---

## ۵. پیوندها و منابع مرتبط

* وب‌سایت و مقالات تخصصی: [molavi.pro](https://molavi.pro)
* مقاله تحلیل استودیو: [molavi.pro/fa/notes/tm-neural-hud-video-studio](https://molavi.pro/fa/notes/tm-neural-hud-video-studio)
* آژانس دیجیتال مارکتینگ: [اینتن آسیا](https://inten.asia)
* فهرست مهارت‌های هوشمند: [MCP Agent Skills Hub](https://github.com/tmolavi/mcp-agent-skills-hub)

---

## ۶. مجوز انتشار

منتشر شده تحت مجوز [MIT](LICENSE).  
حق امتیاز (c) ۲۰۲۶ **تقی مولوی** ([molavi.pro](https://molavi.pro)).

</div>
