import configparser
from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://tanujbhatia0001:qBsaRlUTqMO2xHxN@cluster0.pv2fd.mongodb.net/sample_configuration_db"
mongo = PyMongo(app)

CONFIG_FILE = "SampleConfigFile.txt"

# Function to read and parse config file
def parse_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        data = {section: dict(config.items(section)) for section in config.sections()}
        return data
    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

# Function to store data in MongoDB
def store_in_db(data):
    mongo.db.config_data.insert_one({"data": data})

# Function to fetch stored config data
def fetch_from_db():
    doc = mongo.db.config_data.find_one()
    #doc = mongo.db.config_data.find_one(sort=[("_id", -1)])
    return doc["data"] if doc else {}

@app.route("/get_config", methods=["GET"])
def get_config():
    data = fetch_from_db()
    return jsonify(data)

if __name__ == "__main__":
    config_data = parse_config(CONFIG_FILE)
    if config_data:
        store_in_db(config_data)
        print("Configuration data stored successfully.")
    else:
        print("Failed to parse configuration file.")
    app.run(debug=True)