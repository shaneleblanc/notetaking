from django.db import models
from notetaking.users.models import User


class Note(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s note: %s - %s - created at %s' % (self.owner, self.title, self.body, self.created)
