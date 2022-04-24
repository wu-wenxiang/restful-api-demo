from pecan import hooks
from pecan import make_app

from rest_demo import model
from rest_demo.package.auth import assert_login


class CustomHook(hooks.PecanHook):
    def before(self, state):
        assert_login(state.request)


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=[
            hooks.TransactionHook(
                model.start,
                model.start_read_only,
                model.commit,
                model.rollback,
                model.clear
            ),
            CustomHook()
        ],
        **app_conf
    )
