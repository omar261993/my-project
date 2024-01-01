from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos',null=True,blank=True)
    def __str__(self) -> str:
        return self.name
class Game(models.Model):
    status1=[("Tranding","Tranding"),("Most Played","Most Played")]
    name = models.CharField(max_length=50)
    photo=models.ImageField(upload_to='photos',null=True,blank=True)
    price_before = models.DecimalField(max_digits=4,decimal_places=2)
    price_now = models.DecimalField(max_digits=4,decimal_places=2)
    Game_description = models.TextField(null=True,blank=True)
    count = models.IntegerField()
    Game_id = models.CharField(max_length=50,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    status=models.BooleanField(default=True)
    tag=models.CharField(max_length=50)
    title=models.CharField(max_length=50,choices=status1,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.username