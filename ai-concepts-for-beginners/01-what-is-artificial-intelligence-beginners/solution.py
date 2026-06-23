"""حل تمرين الدرس الثاني: توسيع بيانات التدريب وإعادة التدريب."""

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "ai_tasks.csv"


def main() -> None:
    data = pd.read_csv(DATA_FILE)

    new_examples = pd.DataFrame([
        {"text": "ترجم هذا البريد إلى العربية", "category": "ترجمة"},
        {"text": "اكتشف العناصر الموجودة داخل الصورة", "category": "صور"},
        {"text": "اقترح لي منتجات تناسب ما شاهدته", "category": "توصيات"},
    ])

    data = pd.concat([data, new_examples], ignore_index=True)

    model = Pipeline([
        ("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=2000)),
    ])

    model.fit(data["text"], data["category"])

    test_text = "أريد اقتراح فيديوهات تناسب اهتماماتي"
    prediction = model.predict([test_text])[0]

    print(f"عدد الأمثلة بعد الإضافة: {len(data)}")
    print(f"الوصف: {test_text}")
    print(f"التصنيف المتوقع: {prediction}")


if __name__ == "__main__":
    main()
