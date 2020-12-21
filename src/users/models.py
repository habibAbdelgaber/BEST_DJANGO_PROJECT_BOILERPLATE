from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # With an AbstractUser Now you can customize and add your own user fields!
    pass
