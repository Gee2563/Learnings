from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    # ex: /orders/
    path("", views.index, name="index"),
    # ex: /orders/5/
    path("<int:order_id>/", views.detail, name="detail"),
    # ex: /orders/5/results/
    path("<int:order_id>/ordered/", views.results, name="ordered"),
    # ex: /orders/5/vote/
    path("<int:order_id>/edit/", views.vote, name="edit"),
]

from django.urls import path

from . import views

