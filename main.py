from flask import Flask, request, render_template, flash, redirect
from currency_symbols import CurrencySymbols
import requests, json

app = Flask(__name__) # this the entry point of the project
### add the secret key from config
app.config.from_object('config')


""" start to create routes or endpoints  """
@app.route('/')
def index():
    """only show default page """
    return render_template('index.html')

@app.route('/currencyConversion', methods=['POST'])   
def  currencyConversion():
    # url
    initialCurrency = request.form['from']
    finalCurrency = request.form['to']
    conversionAmount = request.form['amount']
    currencySymbol = CurrencySymbols.get_symbol(finalCurrency)
    print(currencySymbol)
    URL = f'https://api.exchangerate.host/convert?from={initialCurrency}&to={finalCurrency}&amount={conversionAmount}&places=2'
    #apiCall = requests.get(URL)#+from={initialCurrency}&to={finalCurrency}&conversionAmount={amount}&places=2)

    apiCall = requests.get(URL)
    data = apiCall.json()
    endResult = json.dumps(data['result'])

    errors = []
    if len(initialCurrency) != 3 or initialCurrency != initialCurrency.upper() or initialCurrency[0] == initialCurrency[1]:
        errors.append(f'Invalid currency code : {initialCurrency}')
    elif len(finalCurrency)   != 3 or finalCurrency != finalCurrency.upper() or finalCurrency[0] == finalCurrency[1]:
        errors.append(f'Invalid currency code : {finalCurrency}')
    finalAmount = float(conversionAmount)   
    try:
        finalAmount
    except ValueError:
        errors.append(f'Invalid Amount: {finalAmount}') 
    if errors:
        for err in errors:
            flash(err, 'errors') 
        return redirect('/')   
    else:
        return render_template('result.html', result=endResult, currencySymbol=currencySymbol)             



if __name__ == '__main__':
    app.run()

    # app.run(host='0.0.0.0', debug=True, port='6007')

