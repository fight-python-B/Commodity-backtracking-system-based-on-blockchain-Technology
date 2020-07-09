from .models import Text


def addText(text):
    text1 = Text(text=text)
    text1.save()
