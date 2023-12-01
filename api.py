from flask import Flask, request, jsonify
from joblib import load
import ast

app = Flask(__name__)

@app.route('/divorce-svc', methods=['POST'])
def run_python_code():
    print(request.headers)

    data = request.get_json()
    print(data)

    if 'input' in data:
        x = ast.literal_eval(data['input'])
        print(x)
        svc = load('divorce_svc.pkl')
        result = svc.predict_proba(x)[0][1].round(4)

        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid request'})

if __name__ == '__main__':
    app.run()

