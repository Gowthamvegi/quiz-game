from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# print(question_data[0]["text"])


for question in question_data:
    text = question["text"]
    answer = question["answer"]
    question_bank.append(Question(text, answer))


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score/ quiz.question_number}")
