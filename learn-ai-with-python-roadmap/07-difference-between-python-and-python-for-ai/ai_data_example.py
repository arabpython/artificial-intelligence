"""مثال لمسار Python للبيانات والذكاء الاصطناعي.

لا يبني نموذجًا هنا، لكنه يوضح المرحلة التي تسبق تعلم الآلة:
قراءة البيانات وفهمها واستخراج مؤشرات منها.
"""

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    scores = data["score"].to_numpy()

    print(f"\nعدد الطلاب: {len(data)}")
    print(f"متوسط الدرجات: {np.mean(scores):.2f}")
    print(f"أعلى درجة: {np.max(scores)}")
    print(f"أقل درجة: {np.min(scores)}")

    successful = data[data["score"] >= 70]
    print("\nالطلاب الناجحون:")
    print(successful[["name", "score"]].to_string(index=False))


if __name__ == "__main__":
    main()
