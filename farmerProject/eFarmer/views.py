from django.shortcuts import render,redirect
from eFarmer import forms
from eFarmer.models import Users,saleProductTable
# Create your views here.
def index(request):

    form=forms.Login()
    if(request.method=='POST'):
        form=forms.Login(request.POST)
    myc={'formL':form}
    if form.is_valid():
        UserName=form.cleaned_data['UserName']
        Password=form.cleaned_data['Password']
        user=list(Users.objects.filter(emailid=UserName))
        if len(user)>0:
            passStored=user[0].password
            print(passStored)
            if(passStored==Password):
                return redirect('eFarmer:homeFarmer')
        else :
            print("JHGFDSA")
        #print(UserName+" "+Password)

    return render(request,'efarmer/index.html',myc)


def homeFarmer(request):
    return render(request,'efarmer/homeFarmer.html')




def signup(request):
    form=forms.Signup()
    myc={'form':form}
    if(request.method=='POST'):
        form=forms.Signup(request.POST)
    if form.is_valid():
        form.save(commit='True')
        return redirect('eFarmer:homeFarmer')

    return render(request,'eFarmer/signup.html',myc)


def saleProduct(request):
    form=forms.saleByUser()
    myc={'form':form}
    if request.method=='POST':
        form=forms.saleByUser(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('eFarmer:homeFarmer')
    return render(request,'eFarmer/saleProduct.html',myc)

def viewMandiRateList(request):
    return render(request,'eFarmer/viewMandiRateList.html')

def viewSaleItems(request):
    #form=forms.saleProductTable()
    obj=saleProductTable.objects.all()
    myc={'obj':obj}
    return render(request,'eFarmer/viewSaleItems.html',myc)
def logout(request):
    return redirect('eFarmer:index')
def homeVendor(request):
    return render(request,'eFarmer/homeVendor.html')
def addToMandiList(request):
    form=forms.addItemToMandi()
    myc={'form':form}
    if request=='POST':
        form=forms.addItemToMandi(request.POST)
    if form.is_valid():
        t.save(commit=True)
        return redirect('eFarmer/homeVendor')
    return render(request,'eFarmer/addItemToMandi.html',myc)
