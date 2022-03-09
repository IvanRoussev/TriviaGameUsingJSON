from time import time
from question_library import get_questions
from question import get_score
import time




# Didnt have time for this :(

class Game:
    
    def __init__(self, QuestionLibrary):
        """[summary]

        Args:
            QuestionLibrary ([type]): [description]
        """
        self.QuestionLibrary = QuestionLibrary

        category = input("Enter a Category... ")

        difficulty = input("Enter a Difficulty... ")
    
        number = input("Enter number of question you want... ")
        
        while number < 0:
            number = input("Enter number of question you want... ")


        self.questions = get_questions(category, difficulty, number)


    def play(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        print(self.questions)
        print(self.answers)

        start = time.time()
        userInput = input("Enter a geuss 1, 2, 3 or 4")

        options = [1, 2, 3, 4]
        if userInput not in options:
            userInput = input("Enter a geuss 1, 2, 3 or 4")

        end = time.time()

        elapsed = end - start

        totalScore = get_score(elapsed)

        print(totalScore)

        return totalScore

