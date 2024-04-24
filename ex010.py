import requests

from_currency = str(input('Digite a moeda que você quer que seja convertida: ').upper())
to_currency = str(input('Digite agora a moeda para a qual você gostaria de converter: ').upper())
amount_money = float(input('Qual seu saldo na moeda {}? $'.format(from_currency)))

response = requests.get(f'https://api.frankfurter.app/latest?amount={amount_money}&from={from_currency}&to={to_currency}')
print(response.status_code)

print(f'{amount_money} {from_currency} is {response.json()["rates"][to_currency]:.2f} {to_currency}')
