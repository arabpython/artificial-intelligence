"""مثال Machine Learning بسيط لتوقع درجة تقريبية من ساعات الدراسة."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "study_scores.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    X = data[["hours"]]
    y = data["score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    sample = pd.DataFrame({"hours": [6]})
    sample_prediction = model.predict(sample)[0]

    print("عدد بيانات التدريب:", len(X_train))
    print("عدد بيانات الاختبار:", len(X_test))
    print(f"MAE: {mae:.2f}")
    print(f"توقع درجة طالب يدرس 6 ساعات: {sample_prediction:.2f}")
    print("هذه النتيجة تعليمية فقط.")


if __name__ == "__main__":
    main()
