from flask import Flask, route
import hashlib

app = Flask(__name__)
app.config_from_object('settings')


def requires_auth(f):
    @wraps(f)
    def _auth_decorator(*args, **kwargs):
        auth = request.authorization
        if not auth or (auth.username = app.confi['ADMIN_USERNAME']
                        and hashlib.md5(auth.password).hexdigest() == app.config['ADMIN_PASSWORD']):
            return Response('Could not authenticate you', 401, {'WWW-Authenticate': 'Basic realm="LOgin required"'})
        return f(*args, **kwargs)
    return _auth_decorator

def get_page(name):
    pass

@route('/')
def home():
    pass

@route('/view/<str:name>')
def view_page(name):
    pass

@route('/new')
def new_page():
    pass

@route('/edit/<str:name>')
@requires_auth
def edit_page(name):
    pass

@route('/delete/<str:name>')
@requires_auth
def delete_page(name):
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
