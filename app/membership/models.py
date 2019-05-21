from django.db import models
from django.utils import timezone


class Membership(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True, default=None)
    price = models.IntegerField(blank=False, null=False)
    period = models.IntegerField(default=1, blank=True, null=True,help_text='1->Monthly, 2->Quarterly, 3->Half Year, 4->Yearly',choices=((1, 'Monthly'), (2, 'Quarterly'),(3, 'Half Year'),(4, 'Yearly')))
    features = models.CharField(max_length=100)
    # features = SelectMultipleField(max_length=10, choices=TOPPING_CHOICES)
    status = models.IntegerField(default=1, blank=True, null=True,help_text='1->Active, 0->Inactive',choices=((1, 'Active'), (0, 'Inactive')))
    created_on = models.DateTimeField(default=timezone.now) 
    updated_on = models.DateTimeField(default=timezone.now,null=True,blank=True)              
    
    def __str__(self):
        return self.name

    class Meta:         
        db_table = 'membership'