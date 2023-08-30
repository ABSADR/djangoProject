from django.urls import path

from feedback import views

urlpatterns = [

 path('create-feedback/', views.FeedbackCreateView.as_view(), name='create_feedback'),
 path('list-of-feedbacks/', views.FeedbackListView.as_view(), name='list_of_feedbacks'),
 path('update-feedback/<int:pk>/', views.FeedbackUpdateView.as_view(), name='update_feedback'),
]