from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for entry in question_data:
    question = Question(html.unescape(entry['question']), entry['correct_answer'])
    question_bank.append(question)

# for item in question_bank:
#     print(item.text, item.answer)


ts = QuizBrain(question_bank)
while ts.still_has_questions():
    ts.next_question()
print("You've completed the quiz")
print(f'Your final score was: {ts.score}/{ts.question_number}')
