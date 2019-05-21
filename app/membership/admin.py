from django.contrib import admin
from .models import Membership
from feature.models import Feature
from django import forms

# Register your models here.
class MembershipAdminForm(forms.ModelForm):
    feature_set = forms.ModelMultipleChoiceField(queryset=Feature.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Membership
        fields = ('name', 'alias', 'price', 'period','feature_set', 'status', 'created_on', 'updated_on')


class MembershipAdmin(admin.ModelAdmin):
    form = MembershipAdminForm
    def save_model(self, request, obj, form, change): # need to overwrite here for save features as comma separted
        super().save_model(request, obj, form, change)

admin.site.register(Membership, MembershipAdmin)