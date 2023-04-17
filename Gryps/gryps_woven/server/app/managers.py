from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ Manager for users """

    def create_user(self, email, password=None, **kwargs):
        """ Create a new user """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        """ Create a new superuser """
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
