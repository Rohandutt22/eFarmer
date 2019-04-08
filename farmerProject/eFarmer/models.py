from django.db import models

# Create your models here.
class Users(models.Model):
    M='M'
    F='F'
    PROFESSOR='PROFFESSOR'
    MANDI_VENDOR='MANDI_VENDOR'
    FARMER='FARMER'
    SHOPKEEPER='SHOPKEEPER'
    profession_choices=((PROFESSOR,'PROFFESSOR'),
    (MANDI_VENDOR,'MANDI_VENDOR'),
    (FARMER,'FARMER'),
    (SHOPKEEPER,'SHOPKEEPER'),
    )
    gender_choices=((M,'Male'),(F,'Female'),)
    firstName=models.CharField(max_length=256)
    lastName=models.CharField(max_length=256)
    gender=models.CharField(max_length=1,
                            choices=gender_choices)
    emailid=models.EmailField(primary_key=True)
    password=models.CharField(max_length=32)
    typeOfUser=models.CharField(max_length=20,choices=profession_choices)
    phoneNo=models.IntegerField()

    def __str__(self):
        return self.firstName


class PersonSaleIndex(models.Model):
    emailid=models.EmailField(primary_key=True)
    noOfItemsAtSale=models.IntegerField(default=0)

    def __str__(self):
        return self.noOfItemsAtSale


class saleProductTable(models.Model):
    LEASE='L'
    SALE='S'
    RENT='R'
    type_choices=((LEASE,'LEASE'),
    (SALE,'SALE'),
    (RENT,'RENT'),
    )
    productId=models.CharField(max_length=256,
        primary_key=True)
    userId=models.ForeignKey(Users,on_delete=models.PROTECT)
    typeOfSale=models.CharField(max_length=1,choices=type_choices)
    nameOfProduct=models.CharField(max_length=256)
    descriptionOfProduct=models.CharField(max_length=1000)

    def __str__(self):
        return self.nameOfProduct

class Mandi(models.Model):
    mandiId=models.CharField(max_length=50,unique=True)
    mandiName=models.CharField(max_length=100)
    mandiAddress=models.CharField(max_length=250)

    def __str__(self):
        return self.mandiName
class MandiRateList(models.Model):
    mandiId=models.ForeignKey(Mandi,on_delete=models.PROTECT)
    vendorId=models.ForeignKey(Users,on_delete=models.PROTECT)
    nameOfItem=models.CharField(max_length=50)
    maxRequirement=models.IntegerField(default=10)

    def __str__(self):
        return self.nameOfItem
