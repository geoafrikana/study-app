from .models import CustomUser
from django.contrib.auth import authenticate

def email_username_authenticator(username, password):
    try:
        user = CustomUser.objects.get(username = username)
    except CustomUser.DoesNotExist:
        try:
            user = CustomUser.objects.get(email = username)
        except CustomUser.DoesNotExist:
            return None
    return authenticate(username = user.username, password = password)

# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None