from flask import Flask, render_template, request, jsonify
from currency_converter import get_exchange_rate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        from_currency = data['from'].upper()
        to_currency = data['to'].upper()
        amount = float(data['amount'])

        if amount < 0:
            return jsonify({'error': 'Amount must be positive'}), 400

        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate

        return jsonify({
            'result': converted_amount,
            'rate': rate,
            'from': from_currency,
            'to': to_currency,
            'amount': amount
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Conversion failed. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)