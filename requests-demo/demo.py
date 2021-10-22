import requests

# r = requests.get('https://xkcd.com/353')
# r_image = requests.get('https://imgs.xkcd.com/comics/python.png')

# payload = { 'page': 2, 'count': 25 }
# test = requests.get('https://httpbin.org/get', params=payload)

# post_payload = { 'username': 'pedro', 'password': 'testing' }
# test_post = requests.post('https://httpbin.org/post', data=post_payload)

# test_auth = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))


# print(test.text)
# print(test.url)

# print(test_post.text)
# test_post_dict = test_post.json()
# print(test_post_dict['form'])

# print(test_auth.json())

try:
    test_delay = requests.get('https://httpbin.org/delay/5', timeout=3)
    print(test_delay)
except requests.exceptions.Timeout as error:
    print('ERROR DE TIMEOUT\n', error)
