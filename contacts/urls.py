from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
    path('<int:id>/', views.ContactsDetailView.as_view(), name="contact-details")
]