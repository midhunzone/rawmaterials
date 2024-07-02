from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num_tires = int(request.form['num_tires'])
        tread_rubber_cost_per_kg = float(request.form['tread_rubber_cost_per_kg'])
        tread_rubber_weight_per_tire = float(request.form['tread_rubber_weight_per_tire'])
        bonding_gum_cost_per_kg = float(request.form['bonding_gum_cost_per_kg'])
        bonding_gum_weight_per_tire = float(request.form['bonding_gum_weight_per_tire'])
        patches_cost_per_unit = float(request.form['patches_cost_per_unit'])
        envelopes_cost_per_unit = float(request.form['envelopes_cost_per_unit'])
        other_consumables_cost_per_tire = float(request.form['other_consumables_cost_per_tire'])
        
        tread_rubber_cost_per_tire = tread_rubber_cost_per_kg * tread_rubber_weight_per_tire
        bonding_gum_cost_per_tire = bonding_gum_cost_per_kg * bonding_gum_weight_per_tire
        total_raw_material_cost_per_tire = (tread_rubber_cost_per_tire + bonding_gum_cost_per_tire + 
                                            patches_cost_per_unit + envelopes_cost_per_unit + 
                                            other_consumables_cost_per_tire)
        total_raw_material_cost = total_raw_material_cost_per_tire * num_tires
        
        return render_template('index.html', total_raw_material_cost=total_raw_material_cost,
                               total_raw_material_cost_per_tire=total_raw_material_cost_per_tire)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
