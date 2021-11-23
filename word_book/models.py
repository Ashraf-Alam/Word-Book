from django.db import models

#Model Word_Mng
class Word_Mng(models.Model):
    the_word = models.TextField()
    the_mng = models.TextField()

    def __str__(self):
        return f'{ self.the_word} { self.the_mng}'


