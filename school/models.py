from django.db import models
import uuid
# Create your models here.



class Subject(models.Model):

    name = models.CharField(max_length=200)
    mark = models.FloatField(null=True,blank=True)
    gpa = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"
    
    
    def save(self,*args,**kwrgs):
        
        if self.mark <=32:
            self.gpa = 0.00
        
        elif 33<=self.mark<=39: 
            self.gpa = 1.00
            
        elif 40<=self.mark<=49: 
            self.gpa = 2.00
        
        elif 50<=self.mark<=59: 
           self.gpa = 3.25
           
        elif 60<=self.mark<=69: 
           self.gpa = 3.50
           
        elif 70<=self.mark<=79: 
           self.gpa = 4.00
           
        elif 80<=self.mark<=100: 
           self.gpa = 5.00    
           
        super(Subject, self).save(*args, **kwrgs)       
        
class Student(models.Model):

    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name}{self.id}"

class Classes(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    subjects = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
   
    def __str__(self):
        return f"{self.name}{self.id}"
    



