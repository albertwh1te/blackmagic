import django_filters
#  from rest_framework.generics import ListAPIView
from rest_framework import viewsets, mixins,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from houses.models import House, Collection
from searches.serializers import HouseListSerializer,CollectionSerializer
# Create your views here.


class ListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass

class CreateListViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet,
        mixins.CreateModelMixin
):
    pass

        
class HouseFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    dateStart = django_filters.RangeFilter()
    address = django_filters.CharFilter(lookup_type="contains")
    structure = django_filters.CharFilter(lookup_type="contains")
    rent = django_filters.NumberFilter()
    petPolicy = django_filters.NumberFilter()
    deposit = django_filters.NumberFilter()

    class Meta:
        model = House
        fields = ['id', 'address', 'dateStart', 'structure',
                  'rent', 'petPolicy', 'deposit']


class HouseListView(ListViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = House.objects.filter()
    serializer_class = HouseListSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_class = HouseFilter


class CollectionsCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class =  CollectionSerializer
  
    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)


