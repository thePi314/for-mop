from django.conf.urls import url
from api.views.health import HealthCheck
from api.views.news import NewsModelView

urlpatterns = [
    # Utils
    url(r"^health/ping/?$", HealthCheck.as_view(), name="health-ping"),

    url(r"^news/?$", NewsModelView.as_view({'get': 'list'}), name="news"),
    url(r"^news/(?P<pk>[0-9a-f-]+)/?$", NewsModelView.as_view({'get': 'retrieve'}), name="news_by_pk"),
    url(r"^news/manual/?$", NewsModelView.as_view({'get': 'manual_fetch'}), name="news_manual_fetch")

]
