import json
import requests
import msvcrt as m
import datetime


def validate_date(date_text):
    is_correct = True
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        is_correct = False
    return is_correct


def wait():
    m.getch()


print("Current and historical foreign exchange rates published by the European Central Bank" + "\n")
print("The rates are updated daily around 4PM CET.")
print("Powered by Fixer.io" + "\n")

supported_currencies = {'USD': 'US dollar', 'JPY': 'Japanese yen', 'BGN': 'Bulgarian lev', 'CZK': 'Czech koruna',
                        'DKK': 'Danish krone', 'GBP': 'Pound sterling', 'HUF': 'Hungarian forint',
                        'PLN': 'Polish zloty', 'RON': 'Romanian leu', 'SEK': 'Swedish krona', 'CHF': 'Swiss franc',
                        'ISK': 'Icelandic krona', 'NOK': 'Norwegian krone', 'HRK': 'Croatian kuna',
                        'RUB': 'Russian rouble', 'TRY': 'Turkish lira', 'AUD': 'Australian dollar',
                        'BRL': 'Brazilian real', 'CAD': 'Canadian dollar', 'CNY': 'Chinese yuan renminbi',
                        'HKD': 'Hong Kong dollar', 'IDR': 'Indonesian rupiah', 'ILS': 'Israeli shekel',
                        'INR': 'Indian rupee', 'KRW': 'South Korean won', 'MXN': 'Mexican peso',
                        'MYR': 'Malaysian ringgit', 'NZD': 'New Zealand dollar', 'PHP': 'Philippine piso',
                        'SGD': 'Singapore dollar', 'THB': 'Thai baht', 'ZAR': 'South African rand'}

print("Supported Currencies:")
for key, value in supported_currencies.items():
    print(''.join([key, ': ', value]))

while True:

    base_ISO = input('\n' + 'Enter base currency (ISO code): ')
    convert_to_ISO = input('Convert to (ISO code): ')

    if base_ISO.upper() not in supported_currencies or convert_to_ISO.upper() not in supported_currencies:
        print("****ERROR: One of provided ISO codes is not valid!****")
        base_ISO = input('\n' + 'Enter base currency (ISO code): ')
        convert_to_ISO = input('Convert to (ISO code): ')

    amount = input("Amount to convert (leave blank if you want just the exchange rate): ")
    hist_choice = input("Check the historical exchange rate (any day since 1999)? (Y/N): ")

    if hist_choice.upper() == "Y":
        hist_date = input("Enter date in YYYY-MM-DD format: ")
        if validate_date(hist_date):
            url = ''.join(['http://api.fixer.io/', hist_date, '?base=', base_ISO])
        else:
            print("Incorrect date format!")
    elif hist_choice.upper() == 'N':
        url = ''.join(['http://api.fixer.io/latest?base=', base_ISO])

    response = requests.get(url)
    response.raise_for_status()
    exRates = json.loads(response.text)
    e = exRates['rates']

    if hist_choice.upper() == "Y":
        if amount == "":
            print(''.join(
                ['Exchange rate for ', hist_date, ': 1 ', base_ISO.upper(), ' = ', str(e[convert_to_ISO.upper()]), ' ',
                 convert_to_ISO.upper()]))
        else:
            print(''.join(
                ['Using exchange rate for ', hist_date, ': ', amount, ' ', base_ISO.upper(), ' = ',
                 str(round(float(amount) * float(e[convert_to_ISO.upper()]), 2)), ' ', convert_to_ISO.upper()]))
    else:
        if amount == "":
            print(''.join(
                ['Exchange rate for ', exRates['date'], ': 1 ', base_ISO.upper(), ' = ', str(e[convert_to_ISO.upper()]),
                 ' ', convert_to_ISO.upper()]))
        else:
            print(''.join(
                ['Exchange rate for ', exRates['date'], ': 1 ', base_ISO.upper(), ' = ', str(e[convert_to_ISO.upper()]),
                 '', convert_to_ISO.upper()]))
            print(''.join(
                ['Using this exchange rate for: ', amount, ' ', base_ISO.upper(), ' = ',
                 str(round(float(amount) * float(e[convert_to_ISO.upper()]), 2)), ' ', convert_to_ISO.upper()]))

    print("\n" + "Press any key to get another quote." + "\n")

    wait()
