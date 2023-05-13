from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from my_account.models import Profile
# from django.contrib.auth.hashers import check_password


class EmailAuthBackend(BaseBackend):
	"""	Authenticate using e-mail account.	"""
	def authenticate(self, request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
		
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)