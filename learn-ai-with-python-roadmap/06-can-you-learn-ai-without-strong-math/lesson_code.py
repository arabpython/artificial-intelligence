"""الدرس 06: هل يمكن تعلم الذكاء الاصطناعي بدون رياضيات قوية؟

أمثلة عملية على الرياضيات التي يحتاجها المبتدئ:
- المتوسط والانحراف المعياري
- احتمال مبسط
- مصفوفة بيانات باستخدام NumPy
"""

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "student_scores.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)
    scores = data["score"].to_numpy()

    print("البيانات:")
    print(data.to_string(index=False))

    print("\n--- إحصاء أساسي ---")
    print(f"متوسط الدرجات: {np.mean(scores):.2f}")
    print(f"الوسيط: {np.median(scores):.2f}")
    print(f"أعلى درجة: {np.max(scores)}")
    print(f"أقل درجة: {np.min(scores)}")
    print(f"الانحراف المعياري: {np.std(scores):.2f}")

    passed = data[data["score"] >= 70]
    pass_probability = len(passed) / len(data)

    print("\n--- احتمال مبسط ---")
    print(f"عدد الطلاب الناجحين: {len(passed)} من {len(data)}")
    print(f"احتمال اختيار طالب ناجح عشوائيًا: {pass_probability:.0%}")

    print("\n--- مصفوفة بيانات ---")
    features = data[["hours_studied", "attendance", "score"]].to_numpy()
    print(features)
    print("\nكل صف يمثل طالبًا، وكل عمود يمثل خاصية رقمية.")


if __name__ == "__main__":
    main()
