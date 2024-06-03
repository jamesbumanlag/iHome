from django.db import models

class Record(models.Model):

    created_at =  models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    religion =  models.CharField(max_length=50)
    house_street =  models.CharField(max_length=100)
    suburb =  models.CharField(max_length=50)
    state =  models.CharField(max_length=10)
    post_code =  models.CharField(max_length=10)
    country =  models.CharField(max_length=50)
    section =  models.CharField(max_length=50)
    med_background =  models.CharField(max_length=200)
    contact_first =  models.CharField(max_length=50)
    contact_last =  models.CharField(max_length=50)
    contact_number =  models.CharField(max_length=50)
    contact_rel =  models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')