from django.db import models

class daily_bizz(models.Model):
    play_station = models.IntegerField(default=0)
    flash_mem = models.IntegerField(default=0)
    comp_repair = models.IntegerField(default=0)
    #others_define = models.CharField(max_length=100)
    #others_amt = models.IntegerField(default=0)
    date_time = models.DateField()
    

    def __str__(self):

        return "%s" % self.date_time

      #return "%s %s %s %s "%(self.play_station, self.flash_mem, self.comp_repair, self.date_time)
    def above_average(self):
        avr = 300
        x = int(avr)
        return self.play_station >= x
        

class electricity(models.Model):
    daily_reading = models.FloatField(default=0)
    weekly_reading = models.FloatField(default=0)
    amt_deposited = models.IntegerField(default=0)
    date_time = models.DateField()
    


    def __str__(self):
        return "%s" % self.date_time
        #return "%s %s " % (self.daily_reading, self.weekly_reading)

class hard_ware(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    installation_amt = models.IntegerField(default=0)
    date_time = models.DateField()

    def __str__(self):

        return self.item
        #return "%s %s %s %s" % (self.item, self.price, self.installation_amt, self.date_time)
    
    
    

# Create your models here.
