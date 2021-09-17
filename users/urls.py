from django.urls import path,include
from users import views


urlpatterns = [
    path('',views.index,name='api'),
    path('rest/1/<int:id>/<str:url>/',views.ping,name='ping'),
    path('rest/2/<int:id>/<str:url>/',views.get_reservation,name='get_reservation'),
    path('rest/3/<int:id>/<str:url>/',views.create_or_modify_reservation,name='create_or_modify_reservation'),
    path('rest/4/<int:id>/<str:url>/',views.check_in_reservation,name='check_in_reservation'),
    path('rest/5/<int:id>/<str:url>/',views.check_out_reservation,name='check_out_reservation'),
    path('rest/6/<int:id>/<str:url>/',views.get_departures_reservation,name='get_departures_reservation'),
    path('rest/7/<int:id>/<str:url>/',views.add_or_update_guest_in_reservation,name='add_or_update_guest_in_reservation'),
    path('rest/8/<int:id>/<str:url>/',views.send_invoice,name='send_invoice'),
    path('rest/9/',views.pms),

]