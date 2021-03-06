"""This is your typical app, demonstrating usage."""

from flask_jsondash.charts_builder import charts

from flask import (
    Flask,
    session,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NOTSECURELOL'
app.config.update(
    JSONDASH_FILTERUSERS=True,
    JSONDASH_GLOBALDASH=True,
    JSONDASH_GLOBAL_USER='global',
)
app.debug = True
app.register_blueprint(charts)


def _can_delete():
    return False


def _can_clone():
    return True


def _get_username():
    return 'anonymous'


# Config examples.
app.config['JSONDASH'] = dict(
    metadata=dict(
        created_by=_get_username,
        username=_get_username,
    ),
    auth=dict(
        clone=_can_clone,
        delete=_can_delete,
    )
)


@app.route('/', methods=['GET'])
def index():
    """Sample index."""
    return '<a href="/charts">Visit the charts blueprint.</a>'


if __name__ == '__main__':
    app.run(debug=True, port=5002)
