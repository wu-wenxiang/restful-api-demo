from pecan import abort
from pecan import hooks
from pecan import make_app
import re

from rest_demo import model

RE_TOKEN_PATH = re.compile(r'/v\d+/tokens/?', re.IGNORECASE)

class CustomHook(hooks.PecanHook):
    def before(self, state):
        if all([
            RE_TOKEN_PATH.search(state.request.path),
            state.request.method == 'POST'
        ]):
            return
        abort(401, f'please signin')


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
