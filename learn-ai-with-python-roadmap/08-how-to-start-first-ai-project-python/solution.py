"""حل تمرين الدرس الثامن."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "student_scores.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    X = data[["hours", "attendance"]]
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

    new_student = pd.DataFrame(
        {"hours": [5], "attendance": [88]}
    )
    predicted_score = model.predict(new_student)[0]

    print(f"متوسط الخطأ المطلق: {mae:.2f}")
    print(
        "توقع درجة طالب يدرس 5 ساعات وحضوره 88: "
        f"{predicted_score:.2f}"
    )


if __name__ == "__main__":
    main()
