import connexion


from {{ cookiecutter.package_name }}.controllers.health_controller import HealthController
from {{ cookiecutter.package_name }} import util


health_controller = HealthController()


def live():
    return health_controller.live()


def ready():
    return health_controller.ready()