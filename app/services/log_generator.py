import logging 
import random 
import time 

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

messages = [
    ("INFO", "User logged in successfully"),
      ("INFO", "APi request received"),
        ("INFO", "Database connection suessfull"),
          ("WARNING", "High respone time detected"),
            ("WARNING", "Memory usage is high"),
              ("ERROR", "Failed to process API request"),
                ("ERROR", "Database query failed"),
                  ("CRITICAL", "Data connection lost"),
                    
]

def generate_logs():
    level,massage = random.choice(messages)
    if level == "INFO":
        logging.info(massage)
    elif level == "WARNING":
        logging.warning(massage)
    elif level == "ERROR":
        logging.error(massage)
    elif level == "CRITICAL":
        logging.critical(massage)
        
        
if __name__ == "__main__":
    print("Logging started...")
    
    while True:
        generate_logs()
        time.sleep(2)