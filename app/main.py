from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

@app.route('/')
def index():
    return "Financial Data Analyzer"

@app.route('/analyze', methods=['GET'])
def analyze():
    dataset = request.args.get('dataset', 'sample.csv')
    file_path = os.path.join(DATA_DIR, dataset)
    if not os.path.isfile(file_path):
        return jsonify({'error': 'dataset not found'}), 404
    df = pd.read_csv(file_path)
    result = {
        'rows': len(df),
        'columns': list(df.columns),
        'mean': df.mean(numeric_only=True).to_dict()
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
