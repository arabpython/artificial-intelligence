"""الدرس 08: تدريب أول نموذج AI بسيط باستخدام Python.

المشروع يتعلم علاقة تقريبية بين ساعات الدراسة والدرجة.
البيانات تعليمية فقط ولا تستخدم لاتخاذ قرارات حقيقية.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "student_scores.csv"
MODEL_FILE = BASE_DIR / "model.joblib"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    print("\nالقيم الناقصة في كل عمود:")
    print(data.isnull().sum())

    X = data[["hours"]]
    y = data["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    joblib.dump(model, MODEL_FILE)

    print(f"\nعدد صفوف التدريب: {len(X_train)}")
    print(f"عدد صفوف الاختبار: {len(X_test)}")
    print(f"متوسط الخطأ المطلق (MAE): {mae:.2f}")
    print(f"تم حفظ النموذج في: {MODEL_FILE.name}")

    example_prediction = model.predict(pd.DataFrame({"hours": [5]}))
    print(f"توقع درجة طالب يدرس 5 ساعات: {example_prediction[0]:.2f}")


if __name__ == "__main__":
    main()
