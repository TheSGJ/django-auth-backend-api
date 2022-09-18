from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from account.models import Account
from .serializers import UserSerializer


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            email= data['email']
            full_name = data['full_name']
            username = data['username']
            password = data['password']
            re_password = data['re_password']

            if password == re_password:
                if len(password) >= 8:
                    if not ((Account.objects.filter(username=username).exists()) and (Account.objects.filter(email=email).exists())):
                        user = Account.objects.create_user(
                            email=email,
                            full_name=full_name,
                            username=username,
                            password=password,
                        )

                        user.save()

                        if ((Account.objects.filter(username=username).exists()) and (Account.objects.filter(email=email).exists())):
                            return Response(
                                {'success': 'Account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            return Response(
                                {'error': 'Something went wrong when trying to create account'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )
                    else:
                        return Response(
                            {'error': 'Username or Email, already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error': 'Password must be at least 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when trying to register account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoadUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )