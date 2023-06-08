from django.urls import path
from .views import book_list
from . import views

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('ti1/', views.ti1, name='ti1'),
    path('ti2/', views.ti2, name='ti2'),
    path('ti3/', views.ti3, name='ti3'),
    path('tigame/', views.tigame, name='tigame'),

    path('pap1/', views.pap1, name='pap1'),
    path('pap2/', views.pap2, name='pap2'),
    path('pap3/', views.pap3, name='pap3'),
    path('papgame/', views.papgame, name='papgame'),

    path('ttm1/', views.ttm1, name='ttm1'),
    path('ttm2/', views.ttm2, name='ttm2'),
    path('ttm3/', views.ttm3, name='ttm3'),
    path('ttmgame/', views.ttmgame, name='ttmgame'),

    path('wap1/', views.wap1, name='wap1'),
    path('wap2/', views.wap2, name='wap2'),
    path('wap3/', views.wap3, name='wap3'),
    path('wapgame/', views.wapgame, name='wapgame'),

    path('thtb1/', views.thtb1, name='thtb1'),
    path('thtb2/', views.thtb2, name='thtb2'),
    path('thtb3/', views.thtb3, name='thtb3'),
    path('thtbgame/', views.thtbgame, name='thtbgame'),

    path('recommend/', views.recommend, name='recommend'),
]

