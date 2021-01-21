from flask import Flask


def create_app():
    '''
        docstring
    '''

    app = Flask(__name__, static_folder='core/static')

    app.secret_key = '%(2@w2#-#7k)ufq8x)v^$**ttk#&ni6xid6z0&ncy-ee+!orkj'

    # views
    from .views import bp_core
    app.register_blueprint(bp_core)

    return app