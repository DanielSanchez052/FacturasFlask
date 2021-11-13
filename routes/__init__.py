from flask import Blueprint

routes = Blueprint('routes', __name__)

from .customer import *
from .invoice import *
from .auth import *
