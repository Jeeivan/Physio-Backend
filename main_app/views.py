from django.contrib.auth.models import User
from .models import Physio_Form, Treatment
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, Physio_FormSerializer, TreatmentSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)


class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
          

class Physio_FormViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Physio_Form.objects.all()
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

class Physio_FormListByUserView(ListAPIView):
    serializer_class = Physio_FormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Assuming 'user_id' is the parameter in your URL
        return Physio_Form.objects.filter(user_id=user_id)

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

class TreatmentListByPhysioFormView(ListAPIView):
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        physio_form_id = self.kwargs['physio_form_id']
        return Treatment.objects.filter(physio_form_id=physio_form_id)

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
