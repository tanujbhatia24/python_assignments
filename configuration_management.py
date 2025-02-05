from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB
app.config["MONGO_URI"] = "mongodb+srv://tanujbhatia0001:qBsaRlUTqMO2xHxN@cluster0.pv2fd.mongodb.net/sample_configuration_db"
mongo = PyMongo(app)

config_file = "SampleConfigFile.txt"

# Function to read the config file
def parse_config(file_path):
    config_data = {}
    current_section = None

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()  # Remove whitespace
            if not line or line.startswith("#"):  # Skip comments/empty lines
                continue

            if line.startswith("[") and line.endswith("]"):  # Section header
                current_section = line[1:-1]
                config_data[current_section] = {}

            elif "=" in line and current_section:  # Key-value pairs
                key, value = map(str.strip, line.split("=", 1))
                config_data[current_section][key] = value

        return config_data

    except Exception as e:
        print(f"Error reading config file: {e}")
        return None

# Function to store data in MongoDB
def store_in_db(config_data):
    try:
        existing_entry = mongo.db.config_data.find_one({"data": config_data})
        if existing_entry:
            print("Configuration data already exists. Skipping insertion.")
        else:
            mongo.db.config_data.insert_one({"data": config_data})
            print("Configuration data stored successfully.")
    except Exception as e:
        print(f"Error storing data in database: {e}")

# Function to read store data in MongoDB
@app.route("/get_config", methods=["GET"])
def get_config():
    try:
        documents = list(mongo.db.config_data.find())  # Convert cursor to list
        if not documents:
            return jsonify({"message": "No config data found"})

        # Convert MongoDB documents to JSON format
        data = [{"_id": str(doc["_id"]), "data": doc["data"]} for doc in documents]
        return jsonify({"config_data": data})

    except Exception as e:
        print("Error fetching data:", str(e))
        return jsonify({"error": "Internal Server Error"})


# Creating main logic, so that function/code should be available for import and reuse in other programs. 
if __name__ == "__main__":
    try:
        config_data = parse_config(config_file)
        if config_data:
            store_in_db(config_data)
        else:
            print("Failed to parse configuration file.")

        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred in the main program: {e}")