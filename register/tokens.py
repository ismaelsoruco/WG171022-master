from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

#esto te genera un codigo de registro por un tiemp odeterminado... como lo mismo que hace la confirmacion de pasword
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()


