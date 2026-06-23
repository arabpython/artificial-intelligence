"""حل تمرين AI vs Machine Learning."""


def classify_request(message: str) -> str:
    message = message.strip().lower()

    if "صورة" in message:
        return "الطلب مرتبط بالصور."
    if "صوت" in message:
        return "الطلب مرتبط بالصوت."
    if "نص" in message or "مقال" in message:
        return "الطلب مرتبط بالنصوص."
    if "بيانات" in message or "csv" in message:
        return "الطلب مرتبط بتحليل البيانات."

    return "لم أتعرف على نوع الطلب من القواعد الحالية."


print(classify_request("أريد تحويل صوت إلى نص"))

# في train_simple_ml.py يمكن تجربة:
# sample = pd.DataFrame({"hours": [8]})
# الفرق: القاعدة مكتوبة يدويًا، أما نموذج ML فيستنتج علاقة تقريبية من البيانات.
