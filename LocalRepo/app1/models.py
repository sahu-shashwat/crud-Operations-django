from django.db import models

# Create your models here.
class items(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.TextField(max_length=30)
     desc=models.TextField(max_length=30)
     def __str__(self):
          return self.name
class product(models.Model):
     id=models.ForeignKey(items, on_delete=models.CASCADE)
     pid=models.AutoField(primary_key=True)
     name=models.TextField(max_length=20)
     price=models.IntegerField()
     desc=models.TextField(max_length=10)
     quantity=models.IntegerField()
