from django.contrib.auth.models import User, Group
from .models import Cat, Dog, Bird, Physio_Form, Treatment
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, CatSerializer, DogSerializer, BirdSerializer, Physio_FormSerializer, TreatmentSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]

class DogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [permissions.IsAuthenticated]

class BirdViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    permission_classes = [permissions.IsAuthenticated]

class Physio_FormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

class TreatmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]