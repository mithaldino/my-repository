from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('contacting', views.contacting, name='contacting'),
    path('custlogin', views.custlogin, name='custlogin'),
    path('customerlogin', views.customerlogin, name='customerlogin'),
    path('changecustpassword',views.changecustpassword, name='changecustpassword'),
    path('changecustpass',views.updatecustpassword, name='updatecustpassword'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('admlog', views.adminlog, name='adminlog'),
    path('contact', views.contact, name='contact'),
    path('iphonevideo', views.iphonevideo, name='iphonevideo'),
    path('airpodsvideo', views.airpodsvideo, name='airpodsvideo'),
    path('watchvideo', views.watchvideo, name='watchvideo'),
    path('macvideo', views.macvideo, name='macvideo'),
    path('store', views.store, name='store'),
    path('adstore', views.addstore, name='addstore'),
    path('storelist', views.storelist, name='storelist'),
    path('deletestore/<int:storeid>',views.deletestore, name = 'deletestore'),
    path('customer', views.customer, name='customer'),
    path('addcust', views.addcustomer, name='addcustomer'),
    path('getcust/<str:custemail>',views.getcust, name='getcust'),
    path('getcust',views.updatecustomer,name='updatecustomer'),
    path('custlist', views.custlist, name='custlist'),
    path('logout',views.logout, name='logout'),
    path('getstoreitem/<int:storeid>',views.getstoreitem, name = 'getstoreitem'),
    path('getstoreitem/upstore',views.updatestore, name = 'updatestore'),
    path('getimageview/<int:storeid>',views.getimageview, name = 'getimageview'),
    path('addtocartform/<int:storeid>',views.showcartform, name='showcartform'),
    path('addtocartform/addtocarttable',views.addtocart, name='addtocart'),
    path('showcart',views.showcart,name='showcart'),
    path('deletecart_1/<int:cartid>', views.deletecart, name='deletecart'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('orderlist',views.showorders, name='showorders'),
    ]
    
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)