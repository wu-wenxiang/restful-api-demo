from config import *


app['debug'] = True

# sqlalchemy_w = {
#     'url'           : 'mysql://root:@localhost/dbname?charset=utf8&use_unicode=0',
#     'echo'          : False,
#     'echo_pool'     : False,
#     'pool_recycle'  : 3600,
#     'encoding'      : 'utf-8'
# }

# # Master database
# sqlalchemy_w = {
#     'url': 'postgresql+psycopg2://root:@master_host/dbname',
#     'pool_recycle': 3600,
#     'encoding': 'utf-8'
# }

# # Read Only database
# sqlalchemy_ro = {
#     'url': 'postgresql+psycopg2://root:@standby_host/dbname',
#     'pool_recycle': 3600,
#     'encoding': 'utf-8'
# }
