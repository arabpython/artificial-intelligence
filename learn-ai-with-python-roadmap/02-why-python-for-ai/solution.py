"""حل التمرين العملي."""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print(f"عدد الطلاب: {len(data)}")
    print(f"أقل درجة: {data['score'].min()}")
    print(f"أعلى درجة: {data['score'].max()}")

    successful_students = data[data["score"] >= 80]
    print("\nالطلاب الذين حصلوا على 80 أو أكثر:")
    print(successful_students[["name", "score"]].to_string(index=False))


if __name__ == "__main__":
    main()
