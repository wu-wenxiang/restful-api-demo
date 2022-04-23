import os
import platform
import sqlite3


# Server Specific Configurations
server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'rest_demo.controllers.root.RootController',
    'modules': ['rest_demo'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/rest_demo/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'rest_demo': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'pecan': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
        '__force_dict__': True
        }
    }
}

DB_DEFAULT_NAME = 'rest-demo.db'
DB_DEFAULT_PATH = f'/tmp/{DB_DEFAULT_NAME}'  # MAC & Linux
if platform.system() == 'Windows':
    DB_DEFAULT_PATH = os.path.join(os.path.dirname(__file__), DB_DEFAULT_NAME)
sqlalchemy = {
    'url': os.getenv('db_url') or (
        f"sqlite:///{DB_DEFAULT_PATH}?check_same_thread=False"
    ),
    'echo': True
}

# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
