# Energy Comparison Demo

This is a simple Flask application that allows users to select between Gas and Electricity, enter a postal code and annual kWh consumption, and view a comparison of the top three energy suppliers (using sample data).

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

> **Note**: The supplier data in this example is static because scraping live data from Check24 or Verivox was not possible in this environment.
