from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# MongoDB connection (update with your MongoDB details)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["weather_db"]
collection = db["weather_data"]

@app.route('/')
def dashboard():
    # Fetch the latest weather data from MongoDB
    data = list(collection.find().sort("_id", -1).limit(10))
    return render_template('dashboard.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
