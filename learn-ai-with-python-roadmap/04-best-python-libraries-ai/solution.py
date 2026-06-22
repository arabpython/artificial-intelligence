"""حل تمرين الدرس الرابع."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
CHART_FILE = BASE_DIR / "attendance_chart.png"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    average_hours = np.mean(data["hours"].to_numpy())
    successful = data[data["score"] >= 80]

    print(f"متوسط ساعات الدراسة: {average_hours:.2f}")
    print("\nالطلاب الذين حصلوا على 80 أو أكثر:")
    print(successful[["name", "score"]].to_string(index=False))

    plt.figure(figsize=(8, 4.5))
    plt.bar(data["name"], data["attendance"])
    plt.title("Student Attendance")
    plt.xlabel("Students")
    plt.ylabel("Attendance")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    print(f"\nتم حفظ الرسم البياني في: {CHART_FILE.name}")


if __name__ == "__main__":
    main()
