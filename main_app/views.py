from django.contrib.auth.models import User, Group
from .models import Physio_Form, Treatment
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, Physio_FormSerializer, TreatmentSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class Physio_FormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

class Physio_FormAddViewSet(viewsets.ModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()

class Physio_FormUpdateViewSet(viewsets.ModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class Physio_FormDeleteViewSet(viewsets.ModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TreatmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class TreatmentAddViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class TreatmentDeleteViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TreatmentUpdateViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
