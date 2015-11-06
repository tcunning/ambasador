# 
# ./manage.py makemigrations referral
# ./manage.py migrate
#
from django.db import models
from django.db.models import F

class Referral(models.Model):
    name = models.CharField('name', max_length=200, unique=True)
    count = models.PositiveIntegerField('count')
    
    def __str__(self):
        return self.name + "(" + `self.count` + ")"

    def incrementCountNow(self):
        self.count = F('count') + 1
        self.save()
        self.refresh_from_db()

	def saveName(self):
		super(Referral, self).save(update_fields=['name'])
		

# See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/ for
# how to override save (to do extra work)
