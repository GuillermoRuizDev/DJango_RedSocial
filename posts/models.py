""" Posts models. """

# Django

from users.models import Profile
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    """ Post model. """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """ Return title and username """
        #return f'{self.title} by @{self.user.username}'
        return '{} by @{}'.format(self.title, self.user.username)