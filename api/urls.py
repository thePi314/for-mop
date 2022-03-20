from django.conf.urls import url
from api.views.health import HealthCheck

urlpatterns = [
    # Utils
    url(r"^health/ping/?$", HealthCheck.as_view(), name="health-ping")
]
