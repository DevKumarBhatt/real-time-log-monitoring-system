import time
from datetime import datetime

from app.database import SessionLocal
from app.models import Log


LOG_FILE = "logs/application.log"


def save_log_to_database(line):
    try:
        parts = line.split(" - ", 2)

        if len(parts) != 3:
            return

        timestamp_text, level, message = parts

        timestamp = datetime.strptime(
            timestamp_text,
            "%Y-%m-%d %H:%M:%S,%f"
        )

        db = SessionLocal()

        log_entry = Log(
            level=level,
            message=message,
            source="application.log",
            timestamp=timestamp
        )

        db.add(log_entry)
        db.commit()
        db.close()

        print(f"Saved to database: {level} - {message}")

    except Exception as e:
        print(f"Error saving log: {e}")


def monitor_logs():
    print("Log monitor started...")

    with open(LOG_FILE, "r") as file:
        # Start monitoring from the end of the file
        file.seek(0, 2)

        while True:
            line = file.readline()

            if line:
                line = line.strip()

                if line:
                    save_log_to_database(line)

            else:
                time.sleep(1)


if __name__ == "__main__":
    monitor_logs()