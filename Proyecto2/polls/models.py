'''En nuestra aplicación de encuestas, crearemos dos modelos: Pregunta y Elección. 
Una pregunta tiene una pregunta y una fecha de publicación. Una elección tiene dos campos: el texto de la elección y un recuento de votos. 
Cada opción está asociada con una pregunta.


quí, cada modelo está representado por una clase que
 es subclase de django.db.models.Model. 
 Cada modelo tiene una serie de variables de clase, cada una de las cuales 
representa un campo de base de datos en el modelo.
-------------
ojo se importo en proyecto del file djvenv estamos desde el repositorio local (file git )
TAMBIEN 
eclipse con git ,e crea una carpeta de git donde se apropia del proyecto y lo usa
'''
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

'''forin key le dice al dj que cada opcion esta relacionada 
 a una pregunta   votes = models.IntegerField(default=0)'''