from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Default values
DEFAULT_VALUES = {
    'number_of_tires': 100,
    'tread_rubber_cost_per_kg': 200,
    'tread_rubber_weight_per_tire': 12,
    'bonding_gum_cost_per_kg': 150,
    'bonding_gum_weight_per_tire': 2,
    'patches_cost_per_unit': 100,
    'envelopes_cost_per_unit': 5000,
    'other_consumables_cost_per_tire': 25
}

@app.route('/')
def index():
    return render_template('index.html', values=DEFAULT_VALUES)

@app.route('/calculate', methods=['POST'])
def calculate():
    number_of_tires = int(request.form['number_of_tires'])
    tread_rubber_cost_per_kg = float(request.form['tread_rubber_cost_per_kg'])
    tread_rubber_weight_per_tire = float(request.form['tread_rubber_weight_per_tire'])
    bonding_gum_cost_per_kg = float(request.form['bonding_gum_cost_per_kg'])
    bonding_gum_weight_per_tire = float(request.form['bonding_gum_weight_per_tire'])
    patches_cost_per_unit = float(request.form['patches_cost_per_unit'])
    envelopes_cost_per_unit = float(request.form['envelopes_cost_per_unit'])
    other_consumables_cost_per_tire = float(request.form['other_consumables_cost_per_tire'])

    tread_rubber_cost = tread_rubber_cost_per_kg * tread_rubber_weight_per_tire
    bonding_gum_cost = bonding_gum_cost_per_kg * bonding_gum_weight_per_tire
    total_raw_material_cost_per_tire = (
        tread_rubber_cost +
        bonding_gum_cost +
        patches_cost_per_unit +
        envelopes_cost_per_unit +
        other_consumables_cost_per_tire
    )
    total_raw_material_cost = total_raw_material_cost_per_tire * number_of_tires

    # Component costs
    component_costs = [
        {'component': 'Tread Rubber', 'unit_cost': tread_rubber_cost, 'total_cost': tread_rubber_cost * number_of_tires},
        {'component': 'Bonding Gum', 'unit_cost': bonding_gum_cost, 'total_cost': bonding_gum_cost * number_of_tires},
        {'component': 'Patches', 'unit_cost': patches_cost_per_unit, 'total_cost': patches_cost_per_unit * number_of_tires},
        {'component': 'Envelopes', 'unit_cost': envelopes_cost_per_unit, 'total_cost': envelopes_cost_per_unit * number_of_tires},
        {'component': 'Other Consumables', 'unit_cost': other_consumables_cost_per_tire, 'total_cost': other_consumables_cost_per_tire * number_of_tires}
    ]

    return render_template(
        'index.html',
        values=request.form,
        total_raw_material_cost_per_tire=total_raw_material_cost_per_tire,
        total_raw_material_cost=total_raw_material_cost,
        component_costs=component_costs
    )

@app.route('/ads.txt')
def ads():
    return send_from_directory(app.root_path, 'ads.txt')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

