"""حل تمرين الدرس السادس."""

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "student_scores.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)
    scores = data["score"].to_numpy()

    average = np.mean(scores)
    standard_deviation = np.std(scores)

    high_attendance = data[data["attendance"] >= 85]
    high_attendance_probability = len(high_attendance) / len(data)

    feature_matrix = data[["hours_studied", "attendance"]].to_numpy()

    print(f"متوسط الدرجات: {average:.2f}")
    print(f"الانحراف المعياري: {standard_deviation:.2f}")
    print(
        "احتمال اختيار طالب حضوره 85 أو أكثر: "
        f"{high_attendance_probability:.0%}"
    )
    print("\nمصفوفة ساعات الدراسة والحضور:")
    print(feature_matrix)


if __name__ == "__main__":
    main()
