# Day 123 – Python Core Task (Logging, API Parsing, Vehicle Data Handling)

This repository contains the code and resources for **Day 123 Python Core Task**, structured into modular phases that demonstrate **core Python programming**, **logging mechanisms**, **API integration**, and **data parsing** — with a use case around **vehicle information collection** via APIs.

---

## 🧠 Purpose of This Project

The objective of this task is to:

- Strengthen **core Python skills** through real-world use cases
- Understand **logging mechanisms (file & console)**
- Work with **REST APIs** to parse and extract JSON data
- Organize codebase with **clean modular structure**
- Apply Python in practical domains such as **automotive data collection**

---

## 📂 Project Structure

```
DAY123/
├── TASK1/               # Logging modules and raw parsing test
│   ├── module_console_logger.py
│   ├── module_file_logger.py
│   ├── module_log_parser.py
│   ├── reverse.py
│   ├── ygLogs.log
│   ├── parsed.log
│   ├── consoleLogs.log
│
├── TASK2/               # API parsing and structured output
│   ├── api_testing.py
│   ├── JSONparsing.py
│   ├── .env
│
├── TASK3/               # Car data retrieval from API and structured handling
│   ├── car.py
│   ├── garage.py
│   ├── garage_collection.py
│   ├── json_data_parser.py
│   ├── infoLogs.log
│   ├── fileLogs.py
│   ├── error.log
│   ├── .env
│
├── README.md            
```

---

## 🔍 Task-wise Insights

### ✅ TASK1 – Logging and Log Parsing

- Implements **custom file and console logging modules**
- Parses and extracts logs from generated files like `consoleLogs.log` or `ygLogs.log`
- Includes utilities like `reverse.py` for basic string/data manipulation
- Demonstrates foundational **error-level, info-level logging**, and **log reading logic**

---

### ✅ TASK2 – API Integration & JSON Parsing

- Uses APIs to fetch **automobile information** (via endpoints like `https://api.api-ninjas.com/v1/cars?model=`)
- Parses complex JSON responses and extracts fields like:
  - Make, model, transmission, fuel type, mpg stats, etc.
- Secure use of **`.env` for API keys**
- Clean, **exception-handled parsing** to avoid JSON decode issues

---

### ✅ TASK3 – Real-World Vehicle Data Collection System

- Simulates a vehicle garage using:
  - `garage.py`: Represents a **Garage class**
  - `car.py`: Defines a **Car object**
  - `garage_collection.py`: Handles the **collection and operation of multiple cars**
- `json_data_parser.py`: Parses JSON into structured format for storage/logging
- Logs are written to `infoLogs.log` and `error.log`
- Includes fault tolerance, user-defined error handling, and structured data logging

---

## 📦 Packages & Tools Used

- `requests` – for making API calls
- `os`, `dotenv` – for managing environment variables securely
- `logging` – for full logging customization
- `json` – for JSON manipulation and parsing

> ✅ **API Used**:  
> `https://api.api-ninjas.com/v1/cars?model=MODEL_NAME`  
> _(Note: You must place your API key in the `.env` file as `API_KEY=your_key`)_

---

## 🛠️ How to Run

1. **Clone this repo**
2. **Setup virtual environment**
   ```bash
   python -m venv venv
   # Activate:
   source venv/bin/activate       # On Linux/Mac
   .\venv\Scripts\activate        # On Windows
   ```
3. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API Key**
   - Create a `.env` file in TASK2 and TASK3 directories:
     ```env
     API_KEY=your_actual_key_here
     ```
5. **Run each task independently** as:
   ```bash
   python TASK1/module_file_logger.py
   python TASK2/api_testing.py
   python TASK3/garage.py
   ```

---

## 💡 Notes

- `TASK1` can be reused in other projects for standardized logging.
- All logs are organized: `error.log`, `infoLogs.log`, `parsed.log`, etc.
- Handle API failures, empty results, or broken JSON with custom error logs.

---

## 🔐 Security Reminder

This repo contains logging and key parsing examples. If using real keys or writing keyloggers (for education only), **never deploy such tools in production or violate any ethical guidelines**.

---

## 📚 Learning Outcome

By the end of this project, you’ll have:

- Implemented full-scale logging
- Parsed and structured complex JSON responses
- Understood modular design patterns in Python
- Integrated with real-world REST APIs
- Developed basic command-line tools to simulate real use cases

---

Feel free to fork, star, or improve this for your own use!
