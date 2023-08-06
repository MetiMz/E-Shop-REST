from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, full_name, password):
        """
        Creates and saves a User with the given email, fullname of phone number and password.
        """

        if not phone_number:
            raise ValueError('The user must have an phone number')

        if not email:
            raise ValueError('The user must have a email')

        if not full_name:
            raise ValueError('The user must have a full name')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        """
        Creates and saves a Super User with the given email, fullname of phone number and password.
        """

        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user