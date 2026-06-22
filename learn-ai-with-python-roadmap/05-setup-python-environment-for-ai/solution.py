"""حل تمرين تجهيز بيئة Python للذكاء الاصطناعي."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
CHART_FILE = BASE_DIR / "scores_chart.png"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    average_attendance = np.mean(data["attendance"].to_numpy())
    successful_students = data[data["score"] >= 80]

    print(f"عدد الطلاب: {len(data)}")
    print(f"متوسط الحضور: {average_attendance:.2f}%")
    print("\nالطلاب الذين حصلوا على 80 أو أكثر:")
    print(successful_students[["name", "score"]].to_string(index=False))

    plt.figure(figsize=(8, 4.5))
    plt.bar(data["name"], data["score"])
    plt.title("Student Scores")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)

    print(f"\nتم حفظ الرسم البياني في: {CHART_FILE.name}")


if __name__ == "__main__":
    main()
