from django.urls import path

from courier.views import RestaurantListView

urlpatterns = [
    path(
        "restaurants/",
        RestaurantListView.as_view(),
        name="restaurant-list"
    ),
]

