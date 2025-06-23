import requests
import configparser
from payloads import *
from utilities.configurations import *
from utilities.resources import ApiResources

config = getconfig()
print("Config sections:", config.sections())
print("API endpoint from config:", config['API']['endpoint'])  # will fail if 'API' is missing
url = config['API']['endpoint'] + ApiResources.addBook
headers = {'Content-Type': 'application/json'}
addbook_response = requests.post(url, json=addBook("soukjl"), headers=headers, )

print(addbook_response.json())
post_book = addbook_response.json()
print(type(post_book))
print(post_book['ID'])
book_ID = post_book['ID']
# Delete above created book
url_delete = config['API']['endpoint']+ApiResources.deleteBook
delete_book = requests.post(url_delete, json={"ID": book_ID}, headers=headers, )

print(delete_book.status_code)
assert delete_book.status_code == 200
del_response = delete_book.json()
print(del_response)
assert del_response['msg'] == "book is successfully deleted"

se = requests.session()
se.auth = ('Vaidehi-git1', getPassword())

# authentication of API using auth method
# username = "Vaidehi-git1"
url = 'https://github.com/user'
api_auth = se.get(url)
print("{}{}".format("Auth status code:",  api_auth.status_code))
assert api_auth.status_code == 200


url2 = 'https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user/user/repos'
response = se.get(url2)
print("{}{}".format("Response to List-authenticated-user status code:",  response.status_code))
assert response.status_code == 200

