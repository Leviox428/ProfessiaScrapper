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
    
    # Start the Flask server
    app.run(port=5000)

    while True:
        user_input = input("Type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break