from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

from apps.results.models import Country


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a super User with the given email, name and password.
        """
        user = self.create_user(email,
            password=password,
            name=name
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    # Personal info
    email = models.EmailField(primary_key=True, max_length=80)      # Email used by WCA account will override email used for signup
    wca_id = models.CharField(unique=True, max_length=10, null=True)
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, null=True)
    manage_competitions = models.BooleanField(default=False, null=True)

    # OAuth token
    access_token = models.CharField(max_length=80, null=True)
    refresh_token = models.CharField(max_length=80, null=True)
    token_type = models.CharField(max_length=20, null=True)
    token_scope = models.CharField(max_length=50, null=True)
    token_created_at = models.IntegerField(null=True)
    token_expiry = models.IntegerField(null=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = UserManager()

    def fill_personal_info_from_api_dict(self, api_dict):
        self.wca_id = api_dict["me"]["wca_id"]
        self.name = api_dict["me"]["name"]
        self.gender = api_dict["me"]["gender"]
        self.country = Country.get_country_from_iso2(api_dict["me"]["country_iso2"])
        self.email = api_dict["me"]["email"]
        self.date_of_birth = api_dict["me"]["dob"]

    def fill_login_info_from_api_dict(self, api_dict):
        self.access_token = api_dict["access_token"]
        self.refresh_token = api_dict["refresh_token"]
        self.token_type = api_dict["token_type"]
        self.token_scope = api_dict["scope"]
        self.token_created_at = api_dict["created_at"]
        self.token_expiry = api_dict["expires_in"]

    def natural_key(self):
        return 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(" ")[-1]

    def can_manage_comps(self):
        return self.manage_competitions

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f"Name: {self.name}, WCA ID: {self.wca_id}, email: {self.email}"
