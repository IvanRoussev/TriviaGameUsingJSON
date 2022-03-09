import random
import math


class Question:
    """Question class which produces the question and organizes the answer and incorrect answers
    """

    def __init__(self, question: str, correct_answer: str, incorrect_answers: list, category: str, difficulty: str):
        """init function declares functions and makes self.answers

        Args:
            question (str): question that will be asked
            correct_answer (str): [the correct answer out of the list
            incorrect_answers (list): incorrect answer out of the list
            category (str): the category they would like to be asked a question from
            difficulty (str): the difficulty either easy medium or hard

        Raises:
            AttributeError: if self.difficulty isnt in diff_options
        """

        self.question = question
        self.category = category
        self.difficulty = difficulty
        diff_options = ['easy', 'medium', 'hard']

        if self.difficulty not in diff_options:
            raise AttributeError


        self.answers = []
        self.answers.append(correct_answer)

        for items in incorrect_answers:
            self.answers.append(items)

        
        print(self.answers)
        random.shuffle(self.answers)

        self.answer_id = self.answers.index(correct_answer)

    


    def __str__(self):
        """puts everything in an organized string

        Returns:
            [type]: string of answer + mulitple choice (answer + incorrect answers)
        """

        return (f"{self.question}?\n1 {self.answers[0]}\n2 {self.answers[1]}\n3 {self.answers[2]}\n4 {self.answers[3]}")




    def get_score(self, elapsed):
        """takes time elapsed and find score depending on what category and how long they took on question

        Args:
            elapsed ([type]): time it took to answer question

        Returns:
            [type]: score of player
        """

        if self.difficulty == 'easy':
            diff = 1

        if self.difficulty == 'medium':
            diff = 2

        if self.difficulty == 'hard':
            diff = 3


        if elapsed > 5:
            score = 10 * diff

        elif elapsed < 5:
            score = int(diff * (225/elapsed - 7 * elapsed))

        return score