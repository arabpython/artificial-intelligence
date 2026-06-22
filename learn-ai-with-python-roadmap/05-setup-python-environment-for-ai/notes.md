# ملخص الدرس الخامس: تجهيز البيئة

## الأدوات الأساسية

- Python: لغة البرمجة.
- VS Code: محرر الكود.
- Python Extension: إضافة VS Code.
- venv: بيئة افتراضية لكل مشروع.
- pip: تثبيت المكتبات.
- NumPy / Pandas / Matplotlib / scikit-learn: حزمة بداية للذكاء الاصطناعي.

## التسلسل الصحيح

1. أنشئ مجلد المشروع.
2. افتح المجلد في VS Code.
3. أنشئ `.venv`.
4. فعّل البيئة.
5. حدّث pip.
6. ثبّت requirements.txt.
7. اختر Interpreter الخاص بـ `.venv`.
8. شغّل check_environment.py.

## أوامر مهمة

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python check_environment.py
```

## عند ظهور ModuleNotFoundError

- تأكد أن البيئة الافتراضية مفعلة.
- استخدم `python -m pip install اسم_المكتبة`.
- اختر Interpreter الصحيح داخل VS Code.
- أعد تشغيل الطرفية أو VS Code عند الحاجة.
