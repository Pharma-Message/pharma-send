from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CIModelBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        UserModel = get_user_model()
<<<<<<< Updated upstream
=======
        print(type(UserModel))
>>>>>>> Stashed changes
        if username is None:
            username = kwargs[UserModel.USERNAME_FIELD]
        try:
            ci_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{ci_field: username})
        except UserModel.DoesNotExist:
<<<<<<< Updated upstream
            UserModel.set_password(password)
=======
            pass
            #print(type(UserModel))
            #UserModel.set_password(password)
>>>>>>> Stashed changes
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    