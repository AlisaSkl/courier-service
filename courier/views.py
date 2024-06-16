from django.views import generic

from courier.models import Restaurant

class RestaurantListView(generic.ListView):
    model = Restaurant
    queryset = Restaurant.objects.order_by("name")
