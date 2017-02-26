import json
import requests
import msvcrt as m


def wait():
    m.getch()


print(
    "\n" + "Get current and historical foreign exchange rates" + "\n" + "published by the European Central Bank" + "\n")

print("The rates are updated daily around 4PM CET.")
print("Powered by Fixer.io" + "\n")

print("Supported Currencies:" + "\n"
                                "   EUR Euro" + "\n"
                                "   USD US Dollar" + "\n"
                                "   JPY Japanese Yen" + "\n"
                                "   BGN Bulgarian Lev" + "\n"
                                "   CZK Czech Koruna" + "\n"
                                "   DKK Danish Krone" + "\n"
                                "   GBP Pound Sterling" + "\n"
                                "   HUF Hungarian Forint" + "\n"
                                "   PLN Polish Zloty" + "\n"
                                "   RON Romanian Leu" + "\n"
                                "   SEK Swedish Krona" + "\n"
                                "   CHF Swiss Franc" + "\n"
                                "   NOK Norwegian Krone" + "\n"
                                "   HRK Croatian Kuna" + "\n"
                                "   RUB Russian Rouble" + "\n"
                                "   TRY Turkish Lira" + "\n"
                                "   AUD Australian Dollar" + "\n"
                                "   BRL Brazilian Real" + "\n"
                                "   CAD Canadian Dollar" + "\n"
                                "   CNY Chinese Yuan Renminbi" + "\n"
                                "   HKD Hong Kong Dollar" + "\n"
                                "   IDR Indonesian Rupiah" + "\n"
                                "   ILS Israeli Shekel" + "\n"
                                "   INR Indian Rupee" + "\n"
                                "   KRW South Korean Won" + "\n"
                                "   MXN Mexican Peso" + "\n"
                                "   MYR Malaysian Ringgit" + "\n"
                                "   NZD New Zealand Dollar" + "\n"
                                "   PHP Philippine Peso" + "\n"
                                "   SGD Singapore Dollar" + "\n"
                                "   THB Thai Baht" + "\n"
                                "   ZAR South African Rand" + "\n"
                                "   ISK Icelandic Krona - The last rate was published on 3 Dec 2008" + "\n")

while True:

    supported = ["AUD", "CAD", "CHF", "CYP", "CZK", "DKK", "EEK", "GBP", "HKD", "HUF", "ISK", "JPY", "KRW", "LTL",
                 "LVL", "MTL", "NOK", "NZD", "PLN", "ROL", "SEK", "SGD", "SIT", "SKK", "TRL", "ZAR", "EUR", "USD"]

    base = input('Enter base currency (ISO code): ')
    convTo = input('\n' + 'Convert to (ISO code): ')

    if base.upper() not in supported or convTo.upper() not in supported:
        print("\n" + "****ERROR: One of the ISO codes is not valid!****" + "\n")
    else:

        amount = input("\n" + "Amount to convert (leave blank if you want just the exchange rate): ")

        hist = input("\n" + "Check the historical exchange rate (any day since 1999)? (Y/N): ")

        if hist.upper() == "Y":
            histDate = input("Enter date in YYYY-MM-DD format: ")

            url = 'http://api.fixer.io/' + histDate + '?base=' + base
        else:
            url = 'http://api.fixer.io/latest?base=' + base

        response = requests.get(url)
        response.raise_for_status()

        exRates = json.loads(response.text)

        e = exRates['rates']

        if hist.upper() == "Y":
            if amount == "":
                print('\n' + 'Exchange rate for ' + histDate + ': 1 ' + base.upper() + ' = ' + str(
                    e[convTo.upper()]) + ' ' + convTo.upper())
            else:
                print('\n' + 'Using exchange rate for ' + histDate + ': ' + amount + ' ' + base.upper() + ' = ' + str(
                    round(float(amount) * float(e[convTo.upper()]), 2)) + ' ' + convTo.upper())
        else:
            if amount == "":
                print('\n' + 'Exchange rate for ' + exRates['date'] + ': 1 ' + base.upper() + ' = ' + str(
                    e[convTo.upper()]) + ' ' + convTo.upper())
            else:
                print('\n' + 'Exchange rate for ' + exRates['date'] + ': 1 ' + base.upper() + ' = ' + str(
                    e[convTo.upper()]) + ' ' + convTo.upper())
                print('\n' + 'Using this exchange rate for: ' + amount + ' ' + base.upper() + ' = ' + str(
                    round(float(amount) * float(e[convTo.upper()]), 2)) + ' ' + convTo.upper())

        print("\n" + "Press any key to get another quote." + "\n")

    wait()
