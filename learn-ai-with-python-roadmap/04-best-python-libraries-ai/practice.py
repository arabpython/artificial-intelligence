"""تمرين عملي - مكتبات Python للذكاء الاصطناعي.

المطلوب:
1) اقرأ ملف students.csv باستخدام Pandas.
2) احسب متوسط ساعات الدراسة باستخدام NumPy.
3) اطبع أسماء الطلاب الذين حصلوا على 80 أو أكثر.
4) ارسم مخطط أعمدة للحضور attendance.
5) احفظ الرسم باسم attendance_chart.png.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "students.csv"

# اكتب حلك هنا
