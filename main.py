import csv
import requests
import json


with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    url = 'https://api.goshippo.com/customs/declarations/';
    header = {"Content-Type": "application/json", "Authorization":input('enter auth_key \n')}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #API starts here
            #data = ''
            data = {}
            data['contents_type'] = 'MERCHANDISE'
            data['non_delivery_option'] = 'RETURN'
            data['certify'] = True
            data['certify_signer'] = 'abc'
            data['incoterm'] = row[1]
            data['non_delivery_option'] = 'RETURN'
            data['items'] = [{
                    "description": "T-shirt",
                    "quantity": row[0],
                    "net_weight": "0.5",
                    "mass_unit": "lb",
                    "value_amount": "200",
                    "value_currency": "USD",
                    "tariff_number": "",
                    "origin_country": "US"
            }]


            json_data = json.dumps(data)
            print(requests)
            response = requests.post(url, data=json_data,headers=header)
            print(response.content)

            line_count += 1
    print(f'Processed {line_count} lines.')
