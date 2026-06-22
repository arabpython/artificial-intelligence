# الفرق بين تعلم Python العادي وتعلم Python للذكاء الاصطناعي

حزمة تطبيقية مرافقة للدرس السابع من مسار **الذكاء الاصطناعي ببايثون** في **بايثون العرب**.

## رابط الدرس

https://www.arabpython.com/p/difference-between-python-and-python-for-artificial-intelligence.html

## محتويات الحزمة

- `python_basics_example.py`: مثال Python عادي يعتمد على قواعد ثابتة.
- `ai_data_example.py`: مثال مبسط لمسار البيانات باستخدام Pandas.
- `practice.py`: تمرين يساعدك على مقارنة المسارين.
- `solution.py`: حل التمرين.
- `data/students.csv`: بيانات تدريبية صغيرة.
- `notes.md`: خريطة واضحة للمهارات المشتركة والفروقات.
- `requirements.txt`: المتطلبات الخاصة بالمثال.
- `lesson-guide.pdf`: كتيب شرح PDF.
- `.gitignore`: ملفات لا يفضل رفعها إلى GitHub.

## التثبيت

يفضل إنشاء بيئة افتراضية:

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

ثم ثبّت المتطلبات:

```bash
python -m pip install -r requirements.txt
```

## التشغيل

مثال Python العادي:

```bash
python python_basics_example.py
```

مثال مسار البيانات:

```bash
python ai_data_example.py
```

## الفكرة الرئيسية

Python واحدة، لكن مسار الذكاء الاصطناعي يضيف:
- التعامل مع البيانات.
- الإحصاء العملي.
- NumPy وPandas وMatplotlib.
- مفاهيم التدريب والاختبار والتنبؤ.
