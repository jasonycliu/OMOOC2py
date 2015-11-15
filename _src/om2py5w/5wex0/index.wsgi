from bottle import Bottle, run
import sae
app = Bottle()

@app_route('/')
def hello():
    return "Hello, world!- bottle"

application = sae.create_wsgi_app(app)
