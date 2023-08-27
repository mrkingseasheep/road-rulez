import random


class Quiz:
    def __init__(self, screen, game_manager):
        self.screen = screen
        self.gameStateManager = game_manager
        question_file = open("questions.txt", 'r')
        self.question_list = question_file.readlines()
        self.questions = []
        question_file.close()

    def parse_questions(self):
        question = ""
        answer = 0
        answers = []
        for line in self.question_list:
            if line[0] == "! ":
                question = ""


    def run(self):
        pass
