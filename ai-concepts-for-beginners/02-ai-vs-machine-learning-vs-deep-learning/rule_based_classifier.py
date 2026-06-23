"""مثال AI قائم على القواعد: لا يتعلم من البيانات."""


def classify_request(message: str) -> str:
    message = message.strip().lower()

    if "صورة" in message:
        return "الطلب مرتبط بالصور."
    if "نص" in message or "مقال" in message:
        return "الطلب مرتبط بالنصوص."
    if "بيانات" in message or "csv" in message:
        return "الطلب مرتبط بتحليل البيانات."

    return "لم أتعرف على نوع الطلب من القواعد الحالية."


def main() -> None:
    message = input("اكتب طلبًا قصيرًا: ")
    print(classify_request(message))


if __name__ == "__main__":
    main()
