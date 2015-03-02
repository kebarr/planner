from flask import (Flask, abort, current_app, render_template,
                   Blueprint, request)

import planner
from planner.model.connect import TransactionFactory
from planner.model.client import Contact
from planner.model.iteration import Iteration
from planner.model.translate import to_dict, to_model
from planner.flags import Flag
from planner.config import HeadConfig
from planner.add_contact import convert_client_dict_form_json
from planner.add_iteration import convert_iteration_dict_form_json
import json

ui = Blueprint('views', __name__, template_folder='templates')
api = Blueprint('api', __name__, template_folder='templates')
feature = Flag(lambda: abort(404), config=lambda: current_app.config)


def create_app(config=HeadConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(ui)
    app.register_blueprint(api)
    app.transaction = TransactionFactory(
        app.config['DBPATH'], create_all=app.config.get("DBCREATE"))

    return app


@ui.route('/')
@feature
def index():
    return "TODO: fix the templates"


@ui.route('/schedule')
@feature
def schedule():
    return render_template('schedule.html')


@ui.route('/add-engagement')
@feature
def add_engagement():
    return render_template('add-engagement.html')


@ui.route('/clients')
@feature
def clients():
    return render_template("clients.html")


@ui.route('/clients/{{client.id}}')
@feature
def client(client_id):
    return render_template("client.html")


@ui.route('/add-client')
@feature
def add_client():
    return render_template("add-client.html")


@ui.route('/add-iteration')
@feature
def add_iteration():
    iteration = to_dict(Iteration(id=1))
    form_data = convert_iteration_dict_form_json(Iteration(id=1).id)
    with open("planner/static/add_iteration_form.json", 'w') as f:
        json.dump(form_data, f)
    return render_template("add-iteration.html")


#@ui.route('/clients/{{client_id}}/new')
@ui.route('/clients/1/new')
@feature
def add_contact(client_id=1):
    contact = to_dict(Contact(clientid=client_id))
    form_data = convert_client_dict_form_json(contact)
    with open("planner/static/add_contact_form.json", 'w') as f:
        json.dump(form_data, f)
    return render_template('add-contact.html')


# just get data posted first, save to db later
@api.route('/clients/1/add', methods=["POST"])
def save_new_contact():
    form_data = request.form
    contact = to_model(form_data, planner.model.client)
    return render_template("clients.html")


@api.route('/api/schedule/iteration-for-engagement')
@feature
def schedule_iteration_for_engagement(self):
    pass
