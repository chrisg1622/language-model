
class Chapter:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return f"{self.__class__.__name__}(title: '{self.title}', text: '{self.text[:30]}'...)"


