from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserProfileSerializer,PasswordResetSerializer,UserChangePasswordSerializer,SignupSerializer,LoginSerializer,PasswordResetSendEmailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
User = get_user_model()
from django.contrib.auth import authenticate
from accounts.renderers import MyRenderer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class SignupView(APIView):
    renderer_classes = [MyRenderer]
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg': 'User Registered Successfully '},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # data = self.request.data
        # name = data['name']
        # email = data['email']
        # password = data['password']
        # password2 = data['password2']
        # if password == password2:
        #     if User.objects.filter(email=email).exists():
        #         return Response({'error': 'Email already exists Try Differnet One ThankYou'})
        #     else:
        #         if len(password) < 6:
        #             return Response({'error': 'Password must be at least 6 characters'})
        #         else:
        #             user = User.objects.create_user(
        #                 name=name, email=email, password=password)
        #             user.save()
                    
        #             return Response({'success': 'User Account Created Successfully'})
        # else:
        #     return Response({'error': 'Password did not match Please Retype Thankyou'})
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [MyRenderer]
    def post(self,request,formate=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user =authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Loged in Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is Not Valid']}},status=status.HTTP_404_NOT_FOUND)
class UserProfileView(APIView):
    renderer_classes = [MyRenderer]
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,format= None):
        serializer= UserProfileSerializer(request.user)
        # if serializer.is_valid():
        return Response(serializer.data)
        # else: 
class UserChangePassword(APIView):
    renderer_classes = [MyRenderer]
    permission_classes =(permissions.IsAuthenticated,)
    def post(self , request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':"password Change Successfully"})
        return Response(serializer.errors)    
class PasswordResetSendEmailView(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [MyRenderer]
    def post (self,request,format= None):
        serializer = PasswordResetSendEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link sent to this Email plz check Email'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class PasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [MyRenderer]
    def post(self,request, uid,token,format=None):
        serializer = PasswordResetSerializer(data= request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)