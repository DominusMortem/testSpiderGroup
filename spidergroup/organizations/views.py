from .mixins import ListRetrieveViewSet
from .serializers import OrganizationSerializer
from .models import Organization


class OrganizationViewSet(ListRetrieveViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    http_method_names = ('get',)