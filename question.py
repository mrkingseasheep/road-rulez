class Question:
    def __init__(self, question, correct_ans, num_ans, answers):
        self.question = question
        self.correct_ans = correct_ans
        self.num_ans = num_ans
        self.answers = answers

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.correct_ans

    def get_options(self):
        return self.answers
