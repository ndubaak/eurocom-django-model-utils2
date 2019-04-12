from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``date_created`` and ``date_updated`` fields.
    """
    date_created = models.DateTimeField(_('date created'), default=timezone.now, editable=False)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created_by`` and ``updated_by`` fields. To be able to
    save the user's information in the the ``created_by`` and ``updated_by`` fields, the ``user`` argument must be
    set when instantiating the class.

    To user ``UserStampedModel``, the user model needs to be passed in the ``save`` method via ``user``.
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('created by'),
                                   related_name='%(app_label)s_%(class)s_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('updated by'),
                                   related_name='%(app_label)s_%(class)s_updated_by', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UserTimeStampedModel(TimeStampedModel, UserStampedModel):
    """
    An abstract base class model that provides self-updating ``date_created``, ``date_updated``, ``created_by`` and
    ``updated_by`` fields. To be able to save the user's information in the the ``created_by`` and ``updated_by``
    fields, the ``user`` argument must be set when instantiating the class.
    """
    class Meta:
        abstract = True
