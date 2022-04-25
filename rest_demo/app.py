from pecan import hooks
from pecan import make_app

from rest_demo import model
from rest_demo.package import auth


class CustomHook(hooks.PecanHook):
    def before(self, state):
        auth.assert_login(state.request)
        auth.assert_permission(state.request)
        return super().before(state)

    def on_error(self, state, e):
        return super().on_error(state, e)


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
