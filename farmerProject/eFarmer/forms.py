from django import forms
from eFarmer.models import Users,saleProductTable,MandiRateList
class Login(forms.Form):
    UserName=forms.CharField()
    Password=forms.CharField()

class Signup(forms.ModelForm):
     class Meta():
         model=Users
         fields='__all__'
class saleByUser(forms.ModelForm):
    class Meta():
        model=saleProductTable
        fields='__all__'
class addItemToMandi(forms.ModelForm):
    class Meta():
        model=MandiRateList
        fields='__all__'
