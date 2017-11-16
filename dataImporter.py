import django
django.setup()

from polls.models import Question, Choice, Choice2
from django.utils import timezone

with open("data.txt", "r") as file:
    for line in file:
        q = Question(question_text = line, pub_date = timezone.now())
        q.save()

        q.choice_set.create(answer_text = "bardzo negatywne", votes = 0)
        q.choice_set.create(answer_text = "negatywne", votes = 0)
        q.choice_set.create(answer_text = "neutralne", votes = 0)
        q.choice_set.create(answer_text = "pozytywne", votes = 0)
        q.choice_set.create(answer_text = "bardzo pozytywne", votes = 0)

        words = line.split()

        for w in words:
            q.choice2_set.create(answer_text=w, votes=0)

        q.save()
