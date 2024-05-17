from typing import List, Set

class Question:
    def __init__(self, text: str, options: List[str]):
        self.text = text
        self.options = options

class QuestionManager:
    def __init__(self):
        self.questions = []
        self.visited = set()

    def addQuestion(self, question: Question) -> None:
        """
        Add a new question to the list of questions.
        """
        self.questions.append(question)

    def searchNext(self) -> Question:
        """
        Perform search on all the questions, return the first unvisited question.
        If all questions are visited, return None.
        """
        for question in self.questions:
            if question not in self.visited:
                return question
        return None

    def answerNext(self, q: Question) -> Question:
        """
        Give the next question based on the previous one.
        """
        # Mark the current question as visited
        self.visited.add(q)
        # Assuming here that the next question is the next one in the list
        index = self.questions.index(q)
        if index < len(self.questions) - 1:
            return self.questions[index + 1]
        else:
            return None  # No more questions

    def refuse(self, q: Question) -> Question:
        """
        Insert the root question (head) into the visited set.
        """
        self.visited.add(self.questions[0])
        return self.questions[0]

    def answered(self, q: Question) -> None:
        """
        Put the question in the visited set to avoid asking it again.
        """
        self.visited.add(q)

# Example usage:
manager = QuestionManager()

# Add questions
q1 = Question("Do you like apples?", ["Yes", "No", "I am allergic to fruit."])
q2 = Question("What kind of apples do you prefer?", ["Granny Smith", "Honeycrisp", "Fuji"])
manager.addQuestion(q1)
manager.addQuestion(q2)

# Interact with the question manager
current_question = manager.searchNext()
while current_question:
    print("NPC asks:", current_question.text)
    if current_question.options:
        print("Options:", current_question.options)
        user_input = input("Your response: ")
        # Handle user response
        current_question = manager.answerNext(current_question)
    else:
        print("No options available.")
        current_question = None
