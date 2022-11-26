class QuizBrain:
    def __init__(self, que_list):
        self.que_number = 0
        self.que_list = que_list
        self.score = 0

    def next_question(self):
        current_question = self.que_list[self.que_number]
        self.que_number += 1
        user_answer = input(f"Que. {self.que_number}. {current_question.text}: (True/False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("Correct!", end=" ")
            self.score += 1
        else:
            print("Wrong answer.", end=" ")

    def still_has_questions(self):
        if len(self.que_list) > self.que_number:
            return 1
        else:
            print(f"\nFinal score: {self.score}/{len(self.que_list)}")
            return 0

