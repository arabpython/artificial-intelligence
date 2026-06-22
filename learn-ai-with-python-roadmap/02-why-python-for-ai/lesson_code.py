"""درس: لماذا تستخدم Python في الذكاء الاصطناعي؟
مثال بسيط على قراءة بيانات واستخراج معلومات أولية باستخدام Pandas.
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    print("\nمعلومات عن البيانات:")
    print(data.info())

    average_score = data["score"].mean()
    average_hours = data["hours"].mean()

    print(f"\nمتوسط الدرجات: {average_score:.2f}")
    print(f"متوسط ساعات الدراسة: {average_hours:.2f}")

    best_student = data.loc[data["score"].idxmax()]
    print("\nأعلى درجة:")
    print(f"الاسم: {best_student['name']}")
    print(f"الدرجة: {best_student['score']}")


if __name__ == "__main__":
    main()
