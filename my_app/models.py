from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=50)
    
    house_street = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    state  = models.CharField(max_length=20)
    post_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    med_background = models.CharField(max_length=250)
    contact_first = models.CharField(max_length=50)
    contact_last = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    contact_rel = models.CharField(max_length=20)
    
    
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')
    

class PersonalCare(models.Model):
    bathing = models.CharField(max_length=100)
    dressing = models.CharField(max_length=100)
    toileting = models.CharField(max_length=100)


class MobilityAssistance(models.Model):
    transfer = models.CharField(max_length=100)
    walking = models.CharField(max_length=100)
    


class NutritionHydration(models.Model):
    feeding_assistance = models.CharField(max_length=100)
    food_intake =models.CharField(max_length=100)
    fluid_intake = models.CharField(max_length=100)


class HealthMonitoring(models.Model):
    bgl = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    o2 = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)

class Activities(models.Model):
    companionship = models.CharField(max_length=100)
    daily_activities = models.CharField(max_length=100)

class Housekeeping(models.Model):
    bathroom = models.CharField(max_length=100)
    laundry = models.CharField(max_length=100)
    bedroom = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    living = models.CharField(max_length=100)

    
