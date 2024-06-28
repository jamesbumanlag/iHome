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
    
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True,on_delete=models.CASCADE)
    bathing = models.CharField(max_length=100)
    dressing = models.CharField(max_length=100)
    toileting = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name} ')




class MobilityAssistance(models.Model):  
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True,on_delete=models.CASCADE)
    transfer = models.CharField(max_length=100)
    mobility = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name} ')


class NutritionHydration(models.Model):
    date_time = models.DateTimeField('Date/Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True ,on_delete=models.CASCADE)
    feeding_assistance = models.CharField(max_length=100)
    food_intake =models.CharField(max_length=100)
    fluid_intake = models.CharField(max_length=100)
    
    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name}')


class HealthMonitoring(models.Model):
    date_time = models.DateTimeField('Date/Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True, on_delete=models.CASCADE)
    bgl = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    o2 = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name} ')
    

class Activities(models.Model):
    date_time = models.DateTimeField('Date/Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True ,on_delete=models.CASCADE)
    companionship = models.CharField(max_length=100)
    daily_activities = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name} ')

class Housekeeping(models.Model):
    date_time = models.DateTimeField('Date/Time', null=True)
    person = models.ForeignKey(Record, blank=True, null=True, on_delete=models.CASCADE)
    bathroom = models.CharField(max_length=100)
    laundry = models.CharField(max_length=100)
    bedroom = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    living = models.CharField(max_length=100)


    def __str__(self):
        return(f'{self.person.first_name} {self.person.last_name} ')

    
