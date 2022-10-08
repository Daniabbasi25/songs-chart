from django.db import models

# Create your models here.
class Songs(models.Model):
    TW=models.IntegerField( null=True,blank=True)
    LW=models.IntegerField()
    Artist=models.CharField(max_length=300)
    SongTitle=models.CharField(max_length=300)
    Label=models.CharField(max_length=300)
    def __str__(self):
        return str(self.SongTitle)