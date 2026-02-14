from django.utils import timezone
from django.contrib.auth import authenticate
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.generics import CreateAPIView,UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .permissions import CanViewPatient,IsReceptionOrAdmin
from .serializers import SignupSerializer,PatientRegistrationSerializer,PatientUpdateSerializer,PatientListSerializer, PatientDetailSerializer
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)
        
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
                "message": "Login successful",
                "role": user.role,
                "username": user.username,
                "access_token": access_token,
                })

        # Store refresh token in HTTP-only cookie
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,        # True in production (HTTPS)
            samesite="Strict",
        )

        return response
    
class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"error": "No refresh token"}, status=401)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            return Response({"access_token": access_token})

        except TokenError:
            return Response({"error": "Invalid refresh token"}, status=401)


class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out"})
        response.delete_cookie("refresh_token")
        return response


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientRegistrationSerializer
    permission_classes = [IsAuthenticated, IsReceptionOrAdmin]
    
    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'create':
            return PatientRegistrationSerializer
        if getattr(self, 'action', None) in ['update', 'partial_update']:
            return PatientUpdateSerializer
        if getattr(self, 'action', None) == 'list':
            return PatientListSerializer
        if getattr(self, 'action', None) == 'retrieve':
            return PatientDetailSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        # Use broader view permissions for listing/retrieving patients
        if getattr(self, 'action', None) in ['list', 'retrieve']:
            return [permission() for permission in [IsAuthenticated, CanViewPatient]]
        # For create/update/delete, restrict to reception/admin as before
        return [permission() for permission in [IsAuthenticated, IsReceptionOrAdmin]]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

# class PatientRegistrationView(CreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientRegistrationSerializer
#     permission_classes = [IsAuthenticated, IsReceptionOrAdmin]

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


# class PatientUpdateView(UpdateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientUpdateSerializer

#     def perform_update(self, serializer):
#         serializer.save(updated_by=self.request.user)


# class PatientListView(ListAPIView):
#     queryset = Patient.objects.all().order_by("created_at")
#     serializer_class = PatientListSerializer
#     permission_classes = [CanViewPatient, IsAuthenticated]

# class PatientDetailView(RetrieveAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientDetailSerializer
#     permission_classes = [CanViewPatient, IsAuthenticated]

# class PatientDeleteView(DestroyAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientDetailSerializer
#     permission_classes = [IsReceptionOrAdmin, IsAuthenticated]