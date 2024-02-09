from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100,primary_key=True)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments,on_delete = models.CASCADE,default=1)
    doc_image = models.ImageField(upload_to='doctors',default="")

    def __str__(self):
        return 'DR'+ self.doc_name

class Bookings(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models. IntegerField()
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)





        

