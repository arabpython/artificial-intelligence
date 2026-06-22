"""حل التمرين العملي."""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    students_with_5_hours = data[data["hours"] >= 5]
    average_attendance = data["attendance"].mean()
    successful_students = data[data["score"] >= 80]
    lowest_student = data.loc[data["score"].idxmin()]

    print(f"عدد الطلاب الذين درسوا 5 ساعات أو أكثر: {len(students_with_5_hours)}")
    print(f"متوسط الحضور: {average_attendance:.2f}%")

    print("\nالطلاب الذين حصلوا على 80 أو أكثر:")
    print(successful_students[["name", "score"]].to_string(index=False))

    print("\nالطالب صاحب أقل درجة:")
    print(f"الاسم: {lowest_student['name']}")
    print(f"الدرجة: {lowest_student['score']}")


if __name__ == "__main__":
    main()
