from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''
    Handle the '/states_list' route.

    Fetch all State objects from the storage engine, sort them by name,
    and pass them to the '7-states_list.html' template.
    '''
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    '''
    Handle the teardown of the application context.

    This function is called after each request. It closes the current
    SQLAlchemy Session.
    '''
    storage.close()


if __name__ == "__main__":
    '''
    Start the Flask application.

    The application listens on 0.0.0.0, port 5000.
    '''
    app.run(host='0.0.0.0', port=5000)
