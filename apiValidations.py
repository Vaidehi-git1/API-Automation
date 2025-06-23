import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName': 'Rahul Shetty'},)
print(response.text)
print(response.json())
print(type(response.json()))
response_list = response.json()
print(response_list[1]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)
print(response.headers['Content-Type'])
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Logical validations: retrieve the value from the results with 'kavya' value.
for actual_book in response_list:
    if actual_book['isbn'] == 'kavya':
        print(actual_book)
        break

expected_book = {'book_name': 'New ', 'isbn': 'kavya', 'aisle': '5684'}

assert actual_book == expected_book



