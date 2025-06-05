from flask import Flask, render_template, request
from sample_data import SAMPLE_DATA

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        energy_type = request.form.get('energy_type', 'Electricity')
        postal_code = request.form.get('postal_code', '')
        try:
            consumption = float(request.form.get('consumption', 0))
        except ValueError:
            consumption = 0
        monthly_use = consumption / 12
        offers = SAMPLE_DATA.get(energy_type, [])
        for offer in offers:
            total = offer['grundpreis'] + offer['arbeitspreis'] * monthly_use
            results.append({
                'name': offer['name'],
                'arbeitspreis': offer['arbeitspreis'],
                'grundpreis': offer['grundpreis'],
                'total': total
            })
        results = sorted(results, key=lambda x: x['total'])[:3]
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
