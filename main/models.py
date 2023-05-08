from django.db import models

class Science(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number1 = models.BigIntegerField(unique=True, null=True, blank=True)
    phone_number2 = models.BigIntegerField(unique=True, null=True, blank=True)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    age = models.IntegerField()
    status = (
        (1, "News"),
        (2, "Finish"),
        (3, "Delete"),
    )
    type = models.IntegerField(choices=status, default=1)
    free_time = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)

class Bot(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)


class BotDetail(models.Model):
    text = models.TextField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)