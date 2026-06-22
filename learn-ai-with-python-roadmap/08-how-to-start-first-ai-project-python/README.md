# كيف تبدأ أول مشروع ذكاء اصطناعي باستخدام Python؟

حزمة تطبيقية مرافقة للدرس الثامن من مسار **الذكاء الاصطناعي ببايثون** في **بايثون العرب**.

## رابط الدرس

https://www.arabpython.com/2026/06/how-to-start-your-first-ai-project-with-python.html

## محتويات الحزمة

- `train_model.py`: تدريب نموذج بسيط لتوقع درجة الطالب من ساعات الدراسة.
- `predict_score.py`: إدخال عدد ساعات والحصول على توقع من النموذج.
- `practice.py`: تمرين عملي لتعديل المشروع.
- `solution.py`: حل التمرين.
- `data/student_scores.csv`: بيانات تدريبية صغيرة.
- `requirements.txt`: المكتبات المطلوبة.
- `notes.md`: ملخص خطوات مشروع تعلم الآلة الأول.
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

ثم شغّل التوقع:

```bash
python predict_score.py
```

## تنبيه مهم

بيانات الطلاب في هذه الحزمة تعليمية ومصطنعة. لا تستخدم نموذجًا صغيرًا أو بيانات غير كافية لاتخاذ قرارات حقيقية عن الطلاب أو الأشخاص.
