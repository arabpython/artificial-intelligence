# ما هو الذكاء الاصطناعي؟

حزمة تطبيقية مرافقة للدرس الثاني من مسار **الذكاء الاصطناعي ببايثون** في **بايثون العرب**.

## رابط الدرس

https://www.arabpython.com/2026/06/what-is-artificial-intelligence-beginners.html

## محتويات الحزمة

- `train_model.py`: تدريب نموذج مبسط لتصنيف نوع المهمة حسب وصف قصير.
- `predict_task.py`: إدخال وصف بسيط والحصول على نوع المهمة المتوقع.
- `practice.py`: تمرين عملي لتوسيع بيانات التدريب.
- `solution.py`: حل التمرين.
- `data/ai_tasks.csv`: بيانات تعليمية صغيرة ومصطنعة.
- `requirements.txt`: المكتبات المطلوبة.
- `notes.md`: ملخص مفاهيم الدرس.
- `lesson-guide.pdf`: كتيب شرح PDF.
- `.gitignore`: ملفات لا يفضل رفعها إلى GitHub.

## تجهيز البيئة

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## تثبيت المتطلبات

```bash
python -m pip install -r requirements.txt
```

## تشغيل المشروع

أولًا درّب النموذج:

```bash
python train_model.py
```

ثم جرّب توقع نوع المهمة:

```bash
python predict_task.py
```

## تنبيه مهم

هذه الحزمة تعليمية ومصطنعة. النموذج صغير جدًا وهدفه شرح فكرة البيانات والتدريب والتصنيف، وليس اتخاذ قرارات حقيقية أو الاعتماد عليه في تطبيقات حساسة.
