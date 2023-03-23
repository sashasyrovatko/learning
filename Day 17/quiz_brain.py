class QuizBrain:
    def __init__(self, q_list):
        self.questing_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.questing_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.questing_number]
        self.questing_number += 1
        user_answer = input(f"Q{self.questing_number}:{current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You qot it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was :{correct_answer}\n You current score is: {self.score}/ {self.questing_number}")
        print("\n")
