import requests

url = 'http://rahulshettyacademy.com'
cookie = {'visit-month': 'February'}
se = requests.get(url, cookies=cookie)
print(se.history) #shows redirection history
# check url redirections with "Allow redirects to false", write code below.

se_redirect = requests.get(url, allow_redirects=False, cookies=cookie)
print(f"checking redirects for url", {se_redirect})

# Inserting "timeout" for heavy load websites, which takes time to respond, to get correct results

se_timeout = requests.get(url, allow_redirects=False, cookies=cookie, timeout=1)
print(f"inserting timeout attribute while getting website info for heavyloads", {se_timeout})


# send attachments through API

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file':open('C:\\Users\\vtadu\\Downloads\\opposite-words-with\\7tmc_3t8x_201109.jpg', 'rb')}

res_attach = requests.post(url, files=files)
print(f"api with post attachement is:", {res_attach.status_code})
print(f"text for uploaded image on server through api is:", {res_attach.text})
print(se.status_code)
se2 = requests.session()
se2.cookies.update({'visit-month': 'February'})

url2 = "https://httpbin.org/cookies"
ses = se2.get(url2, cookies={'visit-year': '2022'})
print(ses.text)
