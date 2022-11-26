from data import question_data, gk_question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

# for i in question_data:
#     new_que = Question(i["text"], i["answer"])
#     question_bank.append(new_que)

for i in gk_question_data:
    new_que = Question(i["question"], i["correct_answer"])
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)


quiz_gk = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print(f"Current score: {quiz.score}/{len(question_bank)}")

