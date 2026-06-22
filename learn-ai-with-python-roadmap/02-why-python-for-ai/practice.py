"""تمرين عملي

المطلوب:
1) اقرأ ملف students.csv باستخدام Pandas.
2) اطبع عدد الطلاب.
3) اطبع أقل درجة وأعلى درجة.
4) اطبع أسماء الطلاب الذين حصلوا على 80 درجة أو أكثر.
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"

# اكتب حلك هنا
