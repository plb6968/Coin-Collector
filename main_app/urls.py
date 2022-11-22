from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('coins/', views.coins_index, name='index'),
  path('coins/<int:coin_id>/', views.coin_details, name='coin_details'),
  path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
  path('coin/<int:pk>/update/', views.CoinUpdate.as_view(), name='coin_update'),
  path('coin/<int:pk>/delete/', views.CoinDelete.as_view(), name='coin_delete'),
  path('coins.<int:coin_id>/add_material/', views.add_material, name='add_material'),
  path('case/create/', views.CaseCreate.as_view(), name='case_create'),
  path('case/<int:pk>', views.CaseDetail.as_view(), name='case_detail'),
  path('case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case_update'),
  path('case/<int:pk>/delete/', views.CaseDelete.as_view(), name='case_delete'),
  path('case/', views.CaseList.as_view(), name='case_index')
]