from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from courier.models import District, Restaurant, Courier

admin.site.unregister(Group)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "district", ]
    search_fields = ["name", ]
    list_filter = ["district__name", ]


@admin.register(Courier)
class CourierAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "driving_license", ]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields":
                    (
                        "driving_license",
                    )
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields":
                    (
                        "driving_license",
                    )
            }
        ),
    )
