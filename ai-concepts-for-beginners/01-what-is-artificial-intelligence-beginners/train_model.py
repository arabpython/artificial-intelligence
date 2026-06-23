"""الدرس 02: نموذج مبسط لفهم الذكاء الاصطناعي باستخدام Python.

المشروع يصنف وصفًا قصيرًا إلى نوع مهمة: ترجمة، صور، توصيات، أو صوت.
البيانات تعليمية فقط ولا تستخدم لاتخاذ قرارات حقيقية.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "ai_tasks.csv"
MODEL_FILE = BASE_DIR / "model.joblib"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    print("أول صفوف البيانات:")
    print(data.head())

    X = data["text"]
    y = data["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y,
    )

    model = Pipeline([
        ("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=2000)),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(model, MODEL_FILE)

    print(f"\nعدد أمثلة التدريب: {len(X_train)}")
    print(f"عدد أمثلة الاختبار: {len(X_test)}")
    print(f"الدقة التعليمية على عينة الاختبار: {accuracy:.2%}")
    print(f"تم حفظ النموذج في: {MODEL_FILE.name}")

    example = "أريد تحويل هذه الجملة إلى الإنجليزية"
    result = model.predict([example])[0]
    print(f"\nمثال: {example}")
    print(f"التصنيف المتوقع: {result}")


if __name__ == "__main__":
    main()
