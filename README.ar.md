<div dir="rtl" align="right">

# استوديو تيليمتري هود النيورال (`TM-neural-hud-video-studio`)

<div align="center" dir="ltr">

**Deterministic Cyberpunk HUD Telemetry & Video Engine for AI Repositories**  
**محرك تيليمتري سايبربانك قطعي لإنتاج فيديوهات استعراض الأكواد والأنظمة الذكية**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium%20Headless-45ba4b.svg)](https://playwright.dev)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20%2B%20AAC-007808.svg)](https://ffmpeg.org)
[![Author](https://img.shields.io/badge/Author-Taqi%20Molavi-orange.svg)](https://molavi.pro)
[![Agency](https://img.shields.io/badge/Agency-Inten%20Asia-red.svg)](https://inten.asia)

**[English](README.md) | [فارسی](README.fa.md) | [Türkçe](README.tr.md) | [Azərbaycan](README.az.md) | [العربية](README.ar.md)**

<br/>

[![استعراض استوديو هود النيورال](https://molavi.pro/videos/neural-hud/neural-hud-studio-poster.jpg)](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)

*فيديو تيليمتري سايبربانك هندسي عالي الدقة — [مشاهدة البث المباشر عبر خوادم molavi.pro](https://molavi.pro/videos/neural-hud/neural-hud-studio.mp4)*

</div>

---

## ١. نظرة عامة وفلسفة النظام

**TM Neural HUD Video Studio** هو نظام هندسي مؤتمت يحوّل المستودعات البرمجية، والخدمات المصغرة، وتدفقات وكلاء الذكاء الاصطناعي إلى **فيديوهات استعراض تيليمتري تفاعلية بأسلوب سايبربانك وهوليوودي متقدم (HUD)**.

يعتمد النظام على محرك تقدم زمني قطعي ورياضي صارم (`window.seekTo(t)`)، حيث يتم التقاط كل إطار بدقة متناهية عبر متصفح Chromium بدون واجهة (Playwright)، وتمريره مباشرة إلى مشفر FFmpeg بالتزامن مع توليد صوتي إلكتروني لموجات الساب-بيس وإشارات الرادار دون الحاجة لأي ملفات صوتية مسبقة.

### أبرز المزايا الهندسية:
* **توليد إطارات قطعي بالكامل (Zero Hallucinated Frames):** يتم حساب موضع كل جسيم وتدفق في الإطار وفق معادلة رياضية دقيقة (`t = frame_index / fps`) لمنع تقطيع الإطارات.
* **مستودع كود خفيف ونظيف:** تُستضاف مقاطع الفيديو بالكامل على خوادم شبكة توزيع المحتوى [molavi.pro CDN](https://molavi.pro/videos/neural-hud/)، مما يحافظ على خفة مستودع Git وسرعة استنساخه.
* **توليف صوتي برمجي بالكامل:** تُولّد مؤثرات مراكز البيانات وصفارات الرادار آلياً عبر مرشحات FFmpeg بدون عينات صوت خارجية.
* **دعم الأبعاد المتعددة:** إنتاج الفيديوهات بالصيغة الرأسية `9:16` المخصصة للهواتف والريلز، أو الصيغة الأفقية `16:9` المخصصة للتوثيق المكتبي.

---

## ٢. مخطط تدفق المعمارية البرمجية

```
┌────────────────────────────────────────────────────────┐
│             لوحة تحكم التيليمتري (HTML5 / Canvas)       │
│  - كرة جسيمات الشبكة العصبية ثلاثية الأبعاد (فيبوناتشي)  │
│  - نافذة عزل هولوغرافية للأنظمة الفرعية وشاشة رادار     │
│  - ٣ بطاقات لمراقبة صحة وحالة الوحدات البرمجية          │
│  - شريط التيليمتري السفلي ثلاثي الأعمدة:               │
│    [1] التوجيه والسجلات + رسم بياني تفاعلي لمعدل التدفق │
│    [2] المسارات والمقاييس + زمن الاستجابة والذاكرة     │
│    [3] التغييرات الحية في الكود الشجري (Live AST Diff)  │
└──────────────────────────┬─────────────────────────────┘
                           │ window.seekTo(t)
             ┌─────────────┴─────────────┐
             ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐
 │ تدفق الإطارات عبر      │   │  التوليف الصوتي       │
 │ محرك Playwright       │   │  البرمجي في FFmpeg    │
 └───────────┬───────────┘   └───────────┬───────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
            [ حاوية فيديو قياسية (H.264 / AAC) ]
                           │
                           ▼
          [ استضافة وتوزيع عبر CDN molavi.pro ]
```

---

## ٣. الإعدادات الجاهزة والنماذج في منظومة مولوي

| المستودع التقني | المجال والتخصص | رابط الفيديو المباشر | مجلد النموذج |
| :--- | :--- | :--- | :--- |
| **[MWIE](https://github.com/tmolavi/molavi-web-intelligence)** | محرك مولوي لذكاء الويب وتحليل SEO/AEO | [مشاهدة الفيديو](https://molavi.pro/videos/neural-hud/mwie-hud.mp4) | [`examples/mwie/`](examples/mwie/) |
| **[SAGE Audit](https://github.com/tmolavi/sage-audit)** | التدقيق ثلاثي الركائز لمحركات البحث التوليدية | [مشاهدة الفيديو](https://molavi.pro/videos/neural-hud/sage-audit-hud.mp4) | [`examples/sage-audit/`](examples/sage-audit/) |
| **[GEO-Scope](https://github.com/tmolavi/geo-scope)** | مقياس استشهادات محركات الذكاء الاصطناعي | [مشاهدة الفيديو](https://molavi.pro/videos/neural-hud/geo-scope-hud.mp4) | [`examples/geo-scope/`](examples/geo-scope/) |
| **[TM Second Brain](https://github.com/tmolavi/tm-second-brain)** | الذاكرة المحلية الدائمة باستخدام SQLite والمتجهات | [مشاهدة الفيديو](https://molavi.pro/videos/neural-hud/second-brain-hud.mp4) | [`examples/tm-second-brain/`](examples/tm-second-brain/) |

---

## ٤. التشغيل السريع والأوامر

### التثبيت
```bash
git clone https://github.com/tmolavi/TM-neural-hud-video-studio.git
cd TM-neural-hud-video-studio
pip install -e .
playwright install chromium
```

### أمر توليد الفيديو
```bash
python3 scripts/render_video.py \
  --repo mwie \
  --output output/mwie_hud.mp4 \
  --aspect 9:16 \
  --duration 6.0 \
  --fps 24
```

---

## ٥. الروابط والمصادر ذات الصلة

* الموقع والمقالات التقنية: [molavi.pro](https://molavi.pro)
* المقال التحليلي للمشروع: [molavi.pro/ar/notes/tm-neural-hud-video-studio](https://molavi.pro/ar/notes/tm-neural-hud-video-studio)
* التسويق الرقمي المتقدم: [Inten Asia](https://inten.asia)
* دليل مهارات الوكلاء: [MCP Agent Skills Hub](https://github.com/tmolavi/mcp-agent-skills-hub)

---

## ٦. الرخصة

تم النشر تحت رخصة [MIT](LICENSE).  
حقوق النشر (c) ٢٠٢٦ **تقي مولوي** ([molavi.pro](https://molavi.pro)).

</div>
