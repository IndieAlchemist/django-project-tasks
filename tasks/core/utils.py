from django.db.models import ObjectDoesNotExist

import logging
import requests


from . import models
from .decorators import timeout_request


logger = logging.getLogger(__name__)


def sync_user_status(user_id, new_status):
    logger.info(f'User with the id {user_id} changed status to {new_status}')


@timeout_request(num_times=3)
def do_request(address):
    return requests.get(address)    

