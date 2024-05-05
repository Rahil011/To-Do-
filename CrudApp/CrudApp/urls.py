from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Insertdata/',views.Insertdata,name='Insertdata'),
    path('register/',views.register,name='register'),
    path('deldata/<title>',views.deldata,name='deldata'),
    path('viewdata/<title>',views.viewdata,name='viewdata'),
    path('updatedata',views.updatedata,name='updatedata'),
]
