class Question:
    def __init__(self, text, answer):
        self.text = text.replace("&quot;", "")
        self.answer = answer

