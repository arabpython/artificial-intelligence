# -*- coding: utf-8 -*-
"""
حل تمرين الدرس 01
"""

import pandas as pd


def main():
    data = pd.read_csv("data/students.csv")

    print("أول 3 صفوف:")
    print(data.head(3))

    average_hours = data["study_hours"].mean()
    max_score = data["score"].max()

    print("
متوسط ساعات الدراسة:", round(average_hours, 2))
    print("أعلى درجة:", max_score)


if __name__ == "__main__":
    main()
