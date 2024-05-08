"""Configuration for the account holders app."""

from django.apps import AppConfig


class AccountHoldersConfig(AppConfig):
    """AppConfig subclass for configuring the account holders app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_holders'
#pep8 checked