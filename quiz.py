import random
import pygame
import time
import sys
from constants import *
from question import Question


class Quiz:
    def __init__(self, screen, game_manager):
        self.screen = screen
        self.gameStateManager = game_manager
        self.questions = []
        self.CLOCK = pygame.time.Clock()
        self.parse_questions()

    def parse_questions(self):
        question_file = open("questions.txt", 'r')
        while True:
            answers = []
            line = question_file.readline()
            if line == "EOF":
                break
            question = line[2::].removesuffix("\n")
            answer = int(question_file.readline())
            num_answers = int(question_file.readline())
            for ans in range(num_answers):
                answers.append(question_file.readline()[2::].removesuffix("\n"))
            if 4 - num_answers >= 1:
                answers.append("Keep calm and carry on!")
                if 4 - num_answers == 2:
                    answers.append("Drink and drive :D")
            self.questions.append(Question(question, answer, num_answers, answers))
        question_file.close()

    def get_rand_question(self):
        idx = random.randrange(0, len(self.questions))
        return self.questions[idx]

    def debug_print_question(self):
        for q in self.questions:
            print(q.get_question())
            for option in q.get_options():
                print("- ", option)
            print("The correct answer is: ", q.get_options()[q.get_answer()])

    def draw_boxes(self, new_question):
        ANS_BOX = [ANS1, ANS2, ANS3, ANS4]
        pygame.draw.rect(self.screen, LIGHT_GRAY, QUESTION)
        question = QUESTION_FONT.render(new_question.get_question(), True, BLACK)
        self.screen.blit(question, question.get_rect(center=QUESTION.center))

        for opt in new_question.get_options():
            answer_area = ANS_BOX.pop()
            pygame.draw.rect(self.screen, LIGHT_GRAY, answer_area)
            answer = ANSWER_FONT.render(opt, True, BLACK)
            answer_area = answer.get_rect(center=answer_area.center)
            self.screen.blit(answer, answer_area)

        pygame.display.update()

    def run(self):
        new_question = self.get_rand_question()
        self.draw_boxes(new_question)
        done = False
        while True:
            self.CLOCK.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    answer = new_question.get_answer()

                    if ANS1.collidepoint(mouse_pos) and answer == 1:
                        self.show_correct(new_question, True)
                        done = True
                        break
                    elif ANS2.collidepoint(mouse_pos) and answer == 2:
                        self.show_correct(new_question, True)
                        done = True
                        break
                    elif ANS3.collidepoint(mouse_pos) and answer == 3:
                        self.show_correct(new_question, True)
                        done = True
                        break
                    elif ANS4.collidepoint(mouse_pos) and answer == 4:
                        self.show_correct(new_question, True)
                        done = True
                        break
                    elif ANS1.collidepoint(mouse_pos) or ANS2.collidepoint(mouse_pos) or ANS3.collidepoint(mouse_pos) or ANS4.collidepoint(mouse_pos):
                        correct = False
                        self.show_correct(new_question, correct)
                        done = True
                        break
            if done:
                break

    def show_correct(self, new_question, correct):
        ANS_BOX = [ANS1, ANS2, ANS3, ANS4]

        if correct:
            SCREEN.fill(LIGHT_LIGHT_GREEN)
            pygame.draw.rect(self.screen, LIGHT_GREEN, QUESTION)
            question = QUESTION_FONT.render(new_question.get_question(), True, GREEN)
            self.screen.blit(question, question.get_rect(center=QUESTION.center))
        else:
            SCREEN.fill(LIGHT_LIGHT_RED)
            pygame.draw.rect(self.screen, LIGHT_RED, QUESTION)
            question = QUESTION_FONT.render(new_question.get_question(), True, RED)
            self.screen.blit(question, question.get_rect(center=QUESTION.center))


        for i, opt in enumerate(new_question.get_options()):
            answer_area = ANS_BOX.pop()
            if i == new_question.get_answer():
                pygame.draw.rect(self.screen, LIGHT_GREEN, answer_area)
                answer = ANSWER_FONT.render(opt, True, GREEN)
            else:
                pygame.draw.rect(self.screen, LIGHT_RED, answer_area)
                answer = ANSWER_FONT.render(opt, True, RED)
            answer_area = answer.get_rect(center=answer_area.center)
            self.screen.blit(answer, answer_area)

        pygame.display.update()

        time.sleep(3)
        self.gameStateManager.set_state("level")
