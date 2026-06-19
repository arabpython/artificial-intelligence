# -*- coding: utf-8 -*-
"""
الدرس 01: تعلم الذكاء الاصطناعي ببايثون من الصفر
بايثون العرب - Arab Python

هذا المثال يوضح فكرة أولية مهمة:
قبل بناء أي نموذج ذكاء اصطناعي، نحتاج قراءة البيانات وفهمها.
"""

from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/students.csv")


def main():
    # قراءة بيانات الطلاب من ملف CSV
    students = pd.read_csv(DATA_PATH)

    print("أول 5 صفوف من البيانات:")
    print(students.head())

    print("
معلومات سريعة عن البيانات:")
    print(students.info())

    average_score = students["score"].mean()
    average_hours = students["study_hours"].mean()

    print("
متوسط ساعات الدراسة:", round(average_hours, 2))
    print("متوسط الدرجات:", round(average_score, 2))

    # مثال بسيط جدًا لفكرة التوقع، وليس نموذج Machine Learning حقيقي
    expected_score = 5 * 12
    print("
مثال مبسط: إذا درس الطالب 5 ساعات، فقد تكون الدرجة المتوقعة تقريبًا:", expected_score)


if __name__ == "__main__":
    main()
