from django.db import models

class Post (models.Model):
    title = models.TextField()
    content = models.TextField( auto_now_add = True )
    create_date = models.DateField()

    def __str__ (self):
        return self.title