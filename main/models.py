from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField(max_length=200)
    postion = models.CharField(max_length=50)
    DOB = models.DateField()
    marital_status =models.BooleanField(default=False)
    blood_group = models.CharField(max_length=3)
    job_title = models.CharField(max_length=50)
    work_location = models.CharField(max_length=30)
    date_of_joining = models.DateField(auto_now_add=True)
    reporting_to = models.CharField(max_length=50)
    linkedin_link = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_img/')

    def __str__(self):
        return self.employee_name

class Leave(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now_add=True)
    nature_of_leave = models.CharField(max_length=100)
    first_day = models.DateField()
    last_day = models.DateField()
    number_of_days = models.IntegerField()
