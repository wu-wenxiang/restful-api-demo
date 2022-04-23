import os
import platform


# Server Specific Configurations
server = {
    'port': '8081',
    'host': 'localhost'
}

# Pecan Application Configurations
app = {
    'root': 'rest_demo.controllers.root.RootController',
    'modules': ['rest_demo'],
    'static_root': '%(confdir)s/../../public',
    'template_path': '%(confdir)s/../templates',
    'debug': True,
    'errors': {
        '404': '/error/404',
        '__force_dict__': True
    }
}

DB_DEFAULT_NAME = 'rest-demo.db'
DB_DEFAULT_PATH = f'/tmp/{DB_DEFAULT_NAME}'  # MAC & Linux
if platform.system() == 'Windows':
    DB_DEFAULT_PATH = os.path.join(os.path.dirname(__file__), DB_DEFAULT_NAME)

# Master database
sqlalchemy_w = {
    'url': os.getenv('db_url') or (
        f"sqlite:///{DB_DEFAULT_PATH}?check_same_thread=False"
    ),
    'echo': True
}
# Read Only database
sqlalchemy_ro = sqlalchemy_w

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
