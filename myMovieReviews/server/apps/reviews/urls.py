from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

from server.apps.reviews.views import reviews_outline, reviews_create, reviews_details, reviews_update, reviews_delete

urlpatterns = [
    path("", reviews_outline),
    path("reviews/create", reviews_create),
    path("reviews/<int:pk>", reviews_details),
    path("reviews/<int:pk>/update", reviews_update),
    path("reviews/<int:pk>/delete", reviews_delete),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)