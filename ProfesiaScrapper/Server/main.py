from flask import Flask, request, jsonify
from Tasks.webScrapper import WebScrapper
from Tasks.dataWriter import DataWriter
from Routes.routes import dataRoutes
from Firebase.firebaseInitializer import FirebaseInitializer
import schedule
import threading
import time

FirebaseInitializer.Initialize()
app = Flask(__name__)
app.register_blueprint(dataRoutes, url_prefix='/data')

def PerformWebScrapping():
    print("Starting WebScrapping")
    webScrapper = WebScrapper()
    webScrapper.PerformWebScrapping()
    scrappedData = webScrapper.GetJobPostingsAndAverageWages()
    print("Webscrapping done")
    print("Saving data to db")
    dataWriter = DataWriter()
    dataWriter.SaveDataToDB(scrappedData)
    print("Data saved")

def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every(1).hour.do(PerformWebScrapping)

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
                PerformWebScrapping()  # Manually trigger the scraping task
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer is shutting down...")