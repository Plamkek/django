from django.urls import path
from . import views

urlpatterns = [
    path('', views.serials_home, name='serials_home'),
    path('create', views.create, name='create'),
    path('<slug>', views.SerialsDetailView.as_view(), name='serials-detail'),
    path('<int:pk>/update', views.SerialsUpdateView.as_view(), name='serial-update'),
    path('<int:pk>/delete', views.SerialsDeleteView.as_view(), name='serial-delete')
]
