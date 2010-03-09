from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Profile(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    avatar = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __unicode__(self):
        return self.full_name


class Post(models.Model):
    content = models.CharField(max_length=160)
    author = models.ForeignKey(Profile)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.content


