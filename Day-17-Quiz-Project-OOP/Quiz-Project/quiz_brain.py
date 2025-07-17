class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self,user_answer, correct_answer):
        self.question_number += 1
        if user_answer == correct_answer:
            self.score += 1
            print("Your answer is correct!")
        else:
            print("Your answer is wrong!")
        print(f"Right answer is {correct_answer}")
        print(f"Your Score is {self.score}/{self.question_number}")
        print('\n')

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}. {self.question_list[self.question_number].question} (true/false)")
        self.check_answer(answer.lower(),self.question_list[self.question_number].answer.lower())

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

