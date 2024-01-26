from django.contrib.auth.models import User
from .models import Physio_Form, Treatment, Discussion
from rest_framework import viewsets, permissions, generics, serializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, Physio_FormSerializer, TreatmentSerializer, DiscussionSerializer
from datetime import datetime, timedelta
from django.utils import timezone


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': "Welcome to WaitlessWellness—your personalized guide to proactive physiotherapy care! Recognizing the prolonged waiting times within the NHS, we understand the urgency of addressing your health concerns. As a seasoned physiotherapist with two years of experience in the NHS, I am here to bridge the gap between your initial inquiry and your face-to-face appointment. Simply submit a brief query outlining your condition, and I will provide tailored advice to kickstart your treatment journey. Our comprehensive platform doesn't stop there—explore our FAQ section for additional insights and peruse valuable general information to empower your health decisions. Additionally, discover a range of targeted exercises designed to empower you on your path to recovery. Take control of your well-being while navigating the waiting game with WaitlessWellness. Your journey to optimal health begins here."}
       return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.body["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        user = self.request.user
        last_month = timezone.now() - timedelta(days=30)  # Assuming a month is approximately 30 days

        # Check if the user has submitted a form within the last month
        if Physio_Form.objects.filter(user=user, date__gte=last_month).exists():
            raise serializers.ValidationError("You can only submit one Physio_Form per month.")

        serializer.save(treatment_complete=False, user=user)

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

class DiscussionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DiscussionAddViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()