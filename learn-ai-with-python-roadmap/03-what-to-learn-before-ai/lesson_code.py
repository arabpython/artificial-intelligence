"""الدرس 03: ماذا أتعلم قبل دخول مجال الذكاء الاصطناعي؟

مثال تطبيقي صغير يوضح مهارات مهمة قبل Machine Learning:
- قراءة CSV
- فحص البيانات
- حساب المتوسط
- استخراج أعلى وأقل نتيجة
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    print("\nعدد الطلاب:", len(data))
    print("أعمدة البيانات:", ", ".join(data.columns))

    average_score = data["score"].mean()
    highest_score = data["score"].max()
    lowest_score = data["score"].min()

    print(f"\nمتوسط الدرجات: {average_score:.2f}")
    print(f"أعلى درجة: {highest_score}")
    print(f"أقل درجة: {lowest_score}")

    top_student = data.loc[data["score"].idxmax()]
    print("\nالطالب صاحب أعلى درجة:")
    print(f"الاسم: {top_student['name']}")
    print(f"الدرجة: {top_student['score']}")
    print(f"ساعات الدراسة: {top_student['hours']}")


if __name__ == "__main__":
    main()
