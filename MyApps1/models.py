from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=60)
    sal=models.FloatField()
    addr=models.CharField(max_length=60)
    def __str__(self):
        return str(self.eno)+" "+self.ename+" "+str(self.sal)+" "+self.job+" "+self.addr
