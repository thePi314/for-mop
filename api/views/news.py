from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models.news import News
from api.serializers.news import NewsSerializer
from scraper.tasks.news_fetch import initiate_fetch


class NewsModelView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    pagination_class = LimitOffsetPagination
    filterset_fields = {
        'created_at': ['gte', 'lte', 'gt', 'lt'],
    }
    order_fields = "__all__"
    search_fields = ['title']

    @action(detail=True, methods=['get'])
    def manual_fetch(self, request):
        initiate_fetch()
        return Response(status=status.HTTP_204_NO_CONTENT)
