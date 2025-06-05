# Energy Comparison Demo

This is a simple Flask application that allows users to select between Gas and Electricity, enter a postal code and annual kWh consumption, and view a comparison of the top three energy suppliers. The application attempts to retrieve live offers from Check24 and falls back to static sample data if fetching is not possible.

## Running the app

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser to use the app.

> **Note**: The application tries to fetch live data from Check24, but network access may be restricted. If fetching fails, the built-in sample data is used instead.
