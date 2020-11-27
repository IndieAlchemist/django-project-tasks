from django.db.models.signals import pre_save
from django.db.models import ObjectDoesNotExist
from django.dispatch import receiver

import logging

from . import models
from . import utils


@receiver(pre_save, sender=models.CustomUser)
def before_user_save(sender, instance, **kwargs):
    try:
        prev_instance = sender.objects.get(id=instance.id)

        if prev_instance.status != instance.status:
            utils.sync_user_status(instance.id, instance.status)

    except ObjectDoesNotExist as e:
        logging.getLogger("info_logger").info(
            "Signals: creating new instance of "+str(sender))
        return
