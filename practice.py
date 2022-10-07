import requests

NO_QUESTIONS = 10
TYPE_OF_QUESTIONS = 'boolean'

parameters = {
    'amount': NO_QUESTIONS,
    'type': TYPE_OF_QUESTIONS,
}

response = requests.get(url='https://opentdb.com/api.php?', params=parameters)
response.raise_for_status()

question_data = response.json()


print(question_data)