import requests
import misc

token = misc.token
# https://api.telegram.org/bot875686930:AAFV9Smcq0JT6zgTlVgT9FBkjfIEhzASx-M/
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def main():
    dictionary = get_updates()



#      'Той-Той любит пластик. Ммммм хрусть-хрусть.')
#      Это точно!
