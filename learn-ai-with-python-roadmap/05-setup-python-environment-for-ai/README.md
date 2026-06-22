# تجهيز بيئة Python للذكاء الاصطناعي

حزمة تطبيقية مرافقة للدرس الخامس من مسار **الذكاء الاصطناعي ببايثون** في **بايثون العرب**.

## رابط الدرس

https://www.arabpython.com/2026/06/setup-python-environment-for-artificial-intelligence.html

## محتويات الحزمة

- `check_environment.py`: يفحص أن Python والمكتبات الأساسية تعمل.
- `src/read_students.py`: مثال بسيط لقراءة ملف CSV وتحليل درجات الطلاب.
- `practice.py`: تمرين عملي للتأكد من تجهيز البيئة.
- `solution.py`: حل التمرين.
- `requirements.txt`: المكتبات المطلوبة للمشروع.
- `.gitignore`: ملفات لا يفضل رفعها إلى GitHub.
- `data/students.csv`: بيانات تدريبية صغيرة.
- `notes.md`: ملخص خطوات تجهيز البيئة.
- `lesson-guide.pdf`: كتيب شرح PDF.

## المتطلبات

- Python مثبت على جهازك.
- VS Code أو محرر Python مناسب.
- Terminal داخل مجلد المشروع.

## إنشاء البيئة الافتراضية

### Windows

```bash
py -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## تثبيت المكتبات

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## فحص البيئة

```bash
python check_environment.py
```

## تشغيل مثال قراءة البيانات

```bash
python src/read_students.py
```

## ملاحظة

عند استخدام VS Code، اختر مفسر Python الذي يحتوي على `.venv` في مساره.
