import csv
import json
from pathlib import Path


def calculate_stats(csv_path):
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != ["message_id", "text"]:
            raise ValueError("Invalid CSV format")

        messages = list(reader)

    if len(messages) == 0:
        raise ValueError("CSV file is empty")

    total_length = 0
    longest_message = ""

    for message in messages:
        if None in message or message["message_id"] is None or message["text"] is None:
            raise ValueError("Invalid CSV row")

        text = message["text"]

        total_length += len(text)

        if len(text) > len(longest_message):
            longest_message = text

    message_count = len(messages)
    average_length = total_length / message_count

    return {
        "message_count": message_count,
        "average_length": round(average_length, 2),
        "longest_message": longest_message
    }


if __name__ == "__main__":
    csv_path = Path(__file__).parent / "messages.csv"

    summary = calculate_stats(csv_path)

    print("Total messages:", summary["message_count"])
    print("Average message length:", summary["average_length"])
    print("Longest message:", summary["longest_message"])

    with open(csv_path.parent / "summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print("Summary saved to summary.json")