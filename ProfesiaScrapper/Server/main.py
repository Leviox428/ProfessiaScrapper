from flask import Flask, request, jsonify
from Tasks.webScrapper import WebScrapper
import schedule
import threading
import time

app = Flask(__name__)
webScrapper = WebScrapper()
schedule.every(1).hour.do(webScrapper.PerformWebScrapping)

def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # Start the schedule runner in a separate thread
    thread = threading.Thread(target=schedule_runner, daemon=True)
    thread.start()

    server_thread = threading.Thread(target=lambda: app.run(port=5000), daemon=True)
    server_thread.start()
    time.sleep(1)

    try:
        while True:
            user_input = input("Type 'force' to manually trigger the scraping task: ")
            if user_input.lower() == 'force':
                print("Forcing web scraping task...")
                webScrapper.PerformWebScrapping()  # Manually trigger the scraping task
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer is shutting down...")