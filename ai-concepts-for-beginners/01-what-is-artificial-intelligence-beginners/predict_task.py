"""استخدم النموذج المدرب لتوقع نوع مهمة ذكاء اصطناعي من وصف قصير."""

from pathlib import Path

import joblib

BASE_DIR = Path(__file__).parent
MODEL_FILE = BASE_DIR / "model.joblib"


def main() -> None:
    if not MODEL_FILE.exists():
        print("لم يتم العثور على النموذج.")
        print("شغّل train_model.py أولًا لتدريب النموذج وحفظه.")
        return

    text = input("اكتب وصفًا قصيرًا للمهمة: ").strip()
    if not text:
        print("يرجى كتابة وصف للمهمة.")
        return

    model = joblib.load(MODEL_FILE)
    prediction = model.predict([text])[0]

    print(f"نوع المهمة المتوقع: {prediction}")
    print("هذه نتيجة تعليمية مبنية على بيانات صغيرة ومصطنعة.")


if __name__ == "__main__":
    main()
