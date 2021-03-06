from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
      path('user_list/', views.user_list_view, name='user_list'),
      path('quiz/<slug:slug>', views.quiz_view, name='quiz-view'),
      path('card/new/', views.new_card, name='card_form'),
      path('deck/new/', views.new_deck, name='deck_form'),
      path('quiz/<slug:slug>/get_card_data/', views.get_card_data, name='get_card_data'),
]
