"""مثال بسيط لقراءة ملف CSV بعد تجهيز البيئة."""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    print(f"\nعدد الطلاب: {len(data)}")
    print(f"متوسط الدرجات: {data['score'].mean():.2f}")
    print(f"أعلى درجة: {data['score'].max()}")
    print(f"أقل درجة: {data['score'].min()}")


if __name__ == "__main__":
    main()
