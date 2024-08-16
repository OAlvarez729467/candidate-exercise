from behave import fixture, use_fixture
from support.config import API_BASE_URL

@fixture
def init_context(context):
    context.base_url = API_BASE_URL
    context.headers = {
        "Content-Type": "application/json"
    }
    yield context
    # Aquí puedes añadir cualquier limpieza si es necesario después de las pruebas

def before_all(context):
    use_fixture(init_context, context)
    # Aquí se pueden añadir configuraciones adicionales antes de todas las pruebas

def before_feature(context, feature):
    # Configuración antes de ejecutar cada característica
    pass

def before_scenario(context, scenario):
    # Configuración antes de ejecutar cada escenario
    pass

def after_scenario(context, scenario):
    # Limpieza después de cada escenario
    if scenario.status == "failed":
        # Capturar detalles del escenario fallido
        pass

def after_feature(context, feature):
    # Limpieza después de cada característica
    pass

def after_all(context):
    # Limpieza global después de todas las pruebas
    pass
