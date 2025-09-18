🌦️ API Testing Framework - OpenWeather

This project demonstrates **API testing with Python + Pytest** for the [OpenWeather API](https://openweathermap.org/api).


🚀 How to Run

1. Clone the repo:
   
   git clone https://github.com/hasanulkabir_md/api-testing-framework.git
   cd api-testing-framework
````

2. Create a virtual environment & install dependencies:

   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   

3. Run tests:

   pytest

---

📂 Project Structure

```
API-TESTING-FRAMEWORK/
│
├── tests/                  # Test cases
│   └── test_weather_api.py
│
├── requirements.txt        # Dependencies
├── pytest.ini              # Pytest configuration
├── README.md               # Project documentation
└── .gitignore              # Ignore venv, cache, reports
```

---

🛠 Tech Stack

* **Python 3.12**
* **Pytest** for testing
* **Requests** for API calls

