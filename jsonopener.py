import json

with open('week5_lab/trivia.json', 'r') as fp:
    data = json.load(fp)


    i = 0
    questionList = []

    for questions in data:
        questions = data[i]['question']
        questionList.append(questions)
        i += 1



