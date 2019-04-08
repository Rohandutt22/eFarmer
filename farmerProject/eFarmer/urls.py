from django.urls import path
from django.urls import include
from django.conf.urls import url

from eFarmer import views
app_name='eFarmer'
urlpatterns=[
   url(r'^$',views.index,name='index'),
   url(r'^homeFarmer/$',views.homeFarmer,name='homeFarmer'),
   url(r'^signup/$',views.signup,name='signup'),
   url(r'^saleProduct/$',views.saleProduct,name='saleProduct'),
   url(r'^viewMandiRateList/$',views.viewMandiRateList,name='viewMandiRateList'),
   url(r'^viewSaleItems/$',views.viewSaleItems,name='viewSaleItems'),
   url(r'^logout/$',views.logout,name='logout'),
   url(r'^homeVendor/$',views.homeVendor,name='homeVendor'),
    url(r'^addToMandiList/$',views.addToMandiList,name='addToMandiList'),        
]
