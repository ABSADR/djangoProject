from django.urls import path

from trainer import views

urlpatterns=[

    path('create-trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
    path('list-of-trainers/', views.TrainerListView.as_view(), name='list_of_trainers'),
    path('update-trainer/<int:pk>/',views.TrainerUpdateView.as_view(), name='update_trainer'),
    path('delete-trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete_trainer'),
    path('detail-trainer/<int:pk>/' ,views.TrainerDetailView.as_view(), name='detail_trainer'),

]