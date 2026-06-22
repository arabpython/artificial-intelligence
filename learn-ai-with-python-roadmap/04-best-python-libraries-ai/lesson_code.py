"""الدرس 04: أفضل مكتبات Python للذكاء الاصطناعي للمبتدئين.

مثال يجمع بين:
- Pandas لقراءة CSV
- NumPy لحسابات رقمية بسيطة
- Matplotlib لرسم البيانات
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"
CHART_FILE = BASE_DIR / "students_scores_chart.png"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    scores = data["score"].to_numpy()

    print("أول صفوف البيانات:")
    print(data.head())

    print(f"\nعدد الطلاب: {len(data)}")
    print(f"متوسط الدرجات: {np.mean(scores):.2f}")
    print(f"أعلى درجة: {np.max(scores)}")
    print(f"أقل درجة: {np.min(scores)}")

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
