'''En nuestra aplicación de encuestas, crearemos dos modelos: Pregunta y Elección. 
Una pregunta tiene una pregunta y una fecha de publicación. Una elección tiene dos campos: el texto de la elección y un recuento de votos. 
Cada opción está asociada con una pregunta.'''

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)