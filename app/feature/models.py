from django.db import models
from django.utils import timezone


class Feature(models.Model):
    title = models.CharField(max_length=100)
    status = models.IntegerField(default=1, blank=True, null=True,help_text='1->Active, 0->Inactive',choices=((1, 'Active'), (0, 'Inactive')))
    created_on = models.DateTimeField(default=timezone.now) 
    updated_on = models.DateTimeField(default=timezone.now,null=True,blank=True)              
    
    def __str__(self):
        return self.title

    class Meta:         
        db_table = 'Feature'