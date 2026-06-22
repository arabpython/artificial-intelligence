"""حل تمرين الدرس السابع."""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"


def rule_based_decision(score: int) -> str:
    if score >= 70:
        return "ناجح"
    return "يحتاج إلى تحسين"


def main() -> None:
    score = 82
    print(f"قرار قاعدة ثابتة للدرجة {score}: {rule_based_decision(score)}")

    data = pd.read_csv(DATA_FILE)
    average_hours = data["hours_studied"].mean()
    high_attendance = data[data["attendance"] >= 85]

    print(f"\nمتوسط ساعات الدراسة: {average_hours:.2f}")
    print("\nالطلاب أصحاب الحضور 85 أو أكثر:")
    print(high_attendance[["name", "attendance"]].to_string(index=False))

    print("\nتوضيح:")
    print("- قرار النجاح هنا قاعدة ثابتة كتبها المبرمج.")
    print("- قراءة CSV وحساب المتوسط مثال على مرحلة تحليل البيانات قبل بناء نموذج AI.")


if __name__ == "__main__":
    main()
