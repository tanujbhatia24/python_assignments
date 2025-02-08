# 🔥 Python Assignments Repository  

Welcome to my **Python Assignments** repository! 🚀 This repository contains various Python scripts related to **security, system monitoring, and configuration management**.  

## 📂 Project Structure  

- **check_password_strength.py** - A script to check the strength of a given password.  
- **cpu_monitor.py** - Monitors CPU usage and provides real-time updates.  
- **configuration_management.py** - Automates configuration updates for system settings.  
- **SampleConfigFile.txt** - Example configuration file used by the configuration_management.py.  
- **requirements.txt** - Dependencies required for running the scripts.  

## 🔧 Installation & Usage  

### 📥 Clone the Repository  
```bash
git clone https://github.com/tanujbhatia24/python-assignments.git
cd python-assignments
```

## 📦 Install Dependencies
### psutil library in Python can be used to retrieve system information, including CPU usage
```bash
pip install psutil
```

### For DB Error Issue follow below steps 
### Setup Instructions
```bash
1. pip install python-dotenv
```
1. Create a `.env` file in the root directory.
2. Add the required variables ->( e.g. MONGO_SECRET_KEY = "mongodb+srv://USERNAME:PASSWORD@cluster0.pv2fd.mongodb.net/sample_configuration_db" )
3. Make sure to put `.env` under `.gitignore` file so that it should remain safe from commit.
4. Run the application.
