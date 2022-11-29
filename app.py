import requests
from tabulate import tabulate
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

columns = ['CharCode', 'Nominal','Name', 'Value']
valute = res.json()['Valute']

print(list(valute))

frame =[]
print ("{:<10} {:<11} {:<50} {:<10}".format('CharCode', 'Nominal','Name', 'Value' ))
for x in list(valute) :
    #print("{:<10} {:<11} {:<50} {:<10}".format(valute[x]["CharCode"], valute[x]["Nominal"], valute[x]["Name"], valute[x]["Value"]))
    frame.append([valute[x]["CharCode"], valute[x]["Nominal"], valute[x]["Name"], valute[x]["Value"]])

print(tabulate(frame, headers=columns,tablefmt='pipe', stralign='center'))