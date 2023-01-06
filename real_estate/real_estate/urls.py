from listings.views import (
    listing_list,
    listing_retrive,
    listing_create,
    listing_update,
    listing_delete,
)
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', listing_list),
    path('admin/', admin.site.urls),
    path('listings/<id>/', listing_retrive),
    path('listings/<id>/edit/', listing_update),
    path('listings/<id>/delete/', listing_delete),
    path('add-listing/', listing_create),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
