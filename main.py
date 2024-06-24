from flask import Flask, request, render_template, jsonify
from load_data import load_data
from process_data import process_data
from model import build_model
from recommandation import recommend_numbers
#from werkzeug.urls import quote
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('date_input_form.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    dates = request.form.get('date')
    if not dates or len(dates) != 8 or not dates.isdigit():
        return jsonify({"error": "Invalid date format. Please use 'ddmmyyyy'."}), 400

    date = dates[:2] + '/' + dates[2:4] + '/' + dates[4:8]
    df = load_data()
    df = process_data(df)
    knn = build_model(df)
    recommendation = recommend_numbers(knn, date)
    recommendation = [str(x) for x in recommendation]

    return render_template('result_template.html', date=date,
                           boule_1=recommendation[0],
                           boule_2=recommendation[1],
                           boule_3=recommendation[2],
                           boule_4=recommendation[3],
                           boule_5=recommendation[4],
                           etoile_1=recommendation[5],
                           etoile_2=recommendation[6])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
