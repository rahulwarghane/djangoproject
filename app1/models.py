from django.db import models

# Create your models here.

class Student(models.Model):
    # sid = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.IntegerField()
    address = models.CharField(max_length=250)
    age = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.name} --- {self.address}"
    
    def show_details(self):
        return f"""name--{self.name}
        Marks -- {self.marks}
        Address -- {self.address}
        Age-- {self.age}
        """
    
    class Meta:
        db_table = "student"

# class New_test(self):
#     pass
        
# def new_stud(models.Model):
#     height = 