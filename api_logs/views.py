from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer
from operator import itemgetter


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    count_critical = Event.objects.filter(level="1").count()
    count_debug = Event.objects.filter(level="2").count()
    count_error = Event.objects.filter(level="3").count()
    count_warning = Event.objects.filter(level="4").count()
    count_info = Event.objects.filter(level="5").count()
    list_levels = [
        {"level": "critical", "count": count_critical},
        {"level": "debug", "count": count_debug},
        {"level": "error", "count": count_error},
        {"level": "warning", "count": count_warning},
        {"level": "info", "count": count_info},
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ["agent_id__env"]

    search_fields = [
        "level",
        "data",
        "agent_id__env",
        "agent_id__address",
        "agent_id__name",
    ]

    @action(detail=False, methods=["get"])
    def order_by_level(self, request):
        return Response(
            sorted(self.list_levels, key=itemgetter("level"), reverse=False)
        )

    @action(detail=False, methods=["get"])
    def order_by_frequency(self, request):
        return Response(sorted(self.list_levels, key=itemgetter("count"), reverse=True))
