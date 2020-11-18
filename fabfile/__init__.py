from colorama import init
init()

from .docker_deploy import *
from .dockercompose_deploy import *
from .dockerswarm_deploy import *
from .inithostos import *