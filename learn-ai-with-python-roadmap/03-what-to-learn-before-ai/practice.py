"""تمرين عملي - قبل دخول مجال الذكاء الاصطناعي

المطلوب:
1) اقرأ ملف students.csv باستخدام Pandas.
2) اطبع عدد الطلاب الذين درسوا 5 ساعات أو أكثر.
3) اطبع متوسط الحضور attendance.
4) اطبع أسماء الطلاب الذين حصلوا على 80 أو أكثر.
5) اطبع اسم الطالب الذي لديه أقل درجة.
"""

from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "students.csv"

# اكتب حلك هنا
