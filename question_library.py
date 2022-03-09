import json
import numbers
from re import I
import random

class QuestionLibrary:
    """Picks question, difficulty and category depending on what the player wants
    """

    def __init__(self, filename='./trivia.json'):
        """Read json file

        Args:
            filename (str) Defaults to 'week5_lab/trivia.json'.
        """
        with open(filename, 'r') as f:
            self.data = json.load(f)
        




    def get_questions(self, category:str=None, difficulty:str=None, number:int=None):
        """Gets a question from the json file

        Args:
            category (str, optional): picks a catgory from the categories list if not in list it will randomly pick. Defaults to None.
            difficulty (str, optional): picks either easy medium or hard if neither than random. Defaults to None.
            number (int, optional): amount of question that the player would like generated. Defaults to None.
        """
        self.category = category
        self.difficulty = difficulty
        categories = ["General Knowledge", "Science & Nature", "Science", "animals", "Geography", "Science: Computers"]
        diff = ["easy", "medium", "hard"]

        if self.category == None:
            category = random.choice(categories)
        else:
            self.category = category


        if self.difficulty == None:
            difficulty = random.choice(diff)
        else:
            self.difficulty = difficulty


        self.questions = []

        i = -1
        for range in self.data:
            num = 0
            i += 1
            while num <= number and self.data[i]['category'] == category and self.data[i]['difficulty'] == difficulty:
                num += 1

            
                self.questions.append(self.data[i]['question']) 


        self.final_questions = []

        for question in self.questions:
            self.final_questions.append(question)
            if len(self.final_questions) == number:
                break




    def __len__(self):
        """finds the length of the questions list

        Returns:
            [type]: the length of questions
        """
        return len(self.final_questions)




    def get_categories(self):
        """finds all unqiue questions
        """
        cats = ["category", "other"]
        return cats

        
        
        
