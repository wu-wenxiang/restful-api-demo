from pecan.hooks import TransactionHook
from pecan import make_app
from rest_demo import model


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    hooks = [
        TransactionHook(
            model.start,
            model.start_read_only,
            model.commit,
            model.rollback,
            model.clear
        )
    ]

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=hooks,
        **app_conf
    )
