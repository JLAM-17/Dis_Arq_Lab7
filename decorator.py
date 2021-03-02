import requests


def random_number_fake(function):
    def wrapper(number=None):
        if (number == None):
            return function()
        elif isinstance(number, int):
            response = requests.get(f"http://numbersapi.com/{number}")
            return response.content.decode('utf-8')
        elif "-" in number:
            date = number.split('-')
            response = requests.get(
                f"http://numbersapi.com/{date[1]}/{date[0]}/date")
            return response.content.decode('utf-8')
        else:
            return function()
    return wrapper
