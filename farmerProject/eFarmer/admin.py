from django.contrib import admin
from eFarmer.models import Users,saleProductTable,PersonSaleIndex,Mandi,MandiRateList
# Register your models here.
admin.site.register(Users)
admin.site.register(saleProductTable)
admin.site.register(PersonSaleIndex)
admin.site.register(Mandi)
admin.site.register(MandiRateList)
