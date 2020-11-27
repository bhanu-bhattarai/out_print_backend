import requests


def send_sms(mobile, message):
    url_endpoint = 'https://sms.office24by7.com/API/sms.php'
    query_params = {
        'username': '9100533391',
        'password': '10OPotp',
        'from': 'OPDEMY',
        'to': mobile,
        'type': 1,
        'msg': 'Greetings from OurPrint. Please verify'
               ' your mobile number. Your OTP is ' + message
    }
    print(message)
    response = requests.get(url_endpoint, params=query_params)
    print(response.content)
