from django.urls import path

from customer import views

urlpatterns = [
    path('inquiry/', views.InquiryCreateAPIView.as_view()),
]