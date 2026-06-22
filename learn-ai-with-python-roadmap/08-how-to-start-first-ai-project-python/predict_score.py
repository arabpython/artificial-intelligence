"""استخدم النموذج المدرب لتوقع درجة تقريبية من ساعات الدراسة."""

from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).parent
MODEL_FILE = BASE_DIR / "model.joblib"


def main() -> None:
    if not MODEL_FILE.exists():
        print("لم يتم العثور على النموذج.")
        print("شغّل train_model.py أولًا لتدريب النموذج وحفظه.")
        return

    try:
        hours = float(input("أدخل عدد ساعات الدراسة: ").strip())
    except ValueError:
        print("يرجى إدخال رقم صحيح أو عشري.")
        return

    if hours < 0:
        print("عدد الساعات لا يمكن أن يكون سالبًا.")
        return

    model = joblib.load(MODEL_FILE)
    input_data = pd.DataFrame({"hours": [hours]})
    prediction = model.predict(input_data)[0]

    print(f"الدرجة المتوقعة تقريبًا: {prediction:.2f}")
    print("هذه نتيجة تعليمية وليست قرارًا حقيقيًا.")


if __name__ == "__main__":
    main()
