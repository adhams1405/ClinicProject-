from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'), 
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('cancel/<int:id>/cancel',views.cancel_appointment, name='cancel'),    
    
    
]
            
    
   
 




















