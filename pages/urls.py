from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('calc',views.calc,name='calc'),
    path('foods',views.foods,name='food'),
    path('workouts',views.workouts,name='workouts'),
    path('legworkouts',views.legworkouts,name='legworkouts'),
    path('armworkouts',views.armworkouts,name='armworkouts'),
    path('backworkouts',views.backworkouts,name='backworkouts'),
    path('shoulderworkouts',views.shoulderworkouts,name='shoulderworkouts'),
    path('chestworkouts',views.chestworkouts,name='chestworkouts'),

]