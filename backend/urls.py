"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from main_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'physioformadd', views.Physio_FormAddViewSet, basename="addphysioform")
router.register(r'physioformupdate', views.Physio_FormUpdateViewSet, basename="updatephysioform")
router.register(r'physioformdelete', views.Physio_FormDeleteViewSet)
router.register(r'physioform', views.Physio_FormViewSet, basename="physioform")
router.register(r'treatmentsadd', views.TreatmentAddViewSet, basename="addtreatment")
router.register(r'treatmentsdelete', views.TreatmentDeleteViewSet, basename="deletetreatment")
router.register(r'treatmentsupdate', views.TreatmentUpdateViewSet, basename="updatetreatment")
router.register(r'treatments', views.TreatmentViewSet, basename="treatment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('signup/', views.CreateUser.as_view(), name ='signup'),
    path('physioform/user/<int:user_id>/', views.Physio_FormListByUserView.as_view(), name='physioform-list-by-user'),
    path('treatments/physioform/<int:physio_form_id>/', views.TreatmentListByPhysioFormView.as_view(), name='treatments-list-by-physioform'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
