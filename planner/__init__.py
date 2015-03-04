from flask import (Flask, abort, current_app, render_template,
                   Blueprint, request)

import datetime
import time
import planner
from planner.model import Base
from planner.model.connect import TransactionFactory
from planner.model.client import Client, Contact
from planner.model.iteration import Iteration
from planner.model.engagement import Engagement
from planner.model.translate import to_dict, to_model
from planner.flags import Flag
from planner.config import HeadConfig
from planner.form_data.add_contact import convert_client_dict_form_json
from planner.form_data.add_iteration import convert_iteration_dict_form_json
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
    with current_app.transaction() as transaction:
        iterations = transaction.query(Iteration).all()
        #engagements = transaction.query(Engagement).all()
    return render_template('schedule.html', iterations=iterations)#, engagements=engagements)


@ui.route('/add-engagement')
@feature
def add_engagement():
    return render_template('add-engagement.html')


@ui.route('/clients')
@feature
def clients():
    with current_app.transaction() as transaction:
        clients = transaction.query(Client).all()
    return render_template("clients.html", clients=clients)


@ui.route('/clients/<int:client_id>', methods=["GET"])
@feature
def client(client_id):
    with current_app.transaction() as transaction:
        client = transaction.query(Client).get(client_id)
    return render_template("contacts.html", client=client)


@ui.route('/add-client')
@feature
def add_client():
    return render_template("add-client.html")


# eventually need the add_iteration.py script to check next id,
# save that as hidden element and pass in
@ui.route('/add-iteration')
@feature
def add_iteration():
    # currently no point doing like this
    # but as we add things to iterations, may be more useful
    form_data = convert_iteration_dict_form_json()
    with open("planner/static/add_iteration_form.json", 'w') as f:
        json.dump(form_data, f)
    return render_template("add-iteration.html")


@api.route('/iteration/new', methods=["POST"])
def save_new_iteration():
    form_data = request.form
    iteration = to_model(form_data, planner.model.iteration)
    date_string = "".join(iteration.startdate.split("/"))
    try:
        iteration.startdate = datetime.datetime.strptime(date_string,
                                                         "%d%m%Y")
    except ValueError:
        return render_template("add_iteration_validation_error.html")
    with current_app.transaction() as transaction:
        transaction.add(iteration)
    return schedule()



@ui.route('/clients/<int:client_id>/new')
@feature
def add_contact(client_id):
    print client_id
    contact = to_dict(Contact(clientid=client_id))
    form_data = convert_client_dict_form_json(contact)
    filename = "planner/static/add_contact_form_%d.json" % (client_id)
    print filename
    with open(filename, 'w') as f:
        json.dump(form_data, f)
    print client_id
    time.sleep(1)
    return render_template('add-contact.html', clientid=client_id)


@api.route('/clients/<int:client_id>/add', methods=["POST"])
def save_new_contact(client_id):
    form_data = request.form
    contact = to_model(form_data, planner.model.client)
    with current_app.transaction() as transaction:
        transaction.add(contact)
        client = transaction.query(Client).get(client_id)
    return render_template("contacts.html", client=client)


@api.route('/api/schedule/iteration-for-engagement')
@feature
def schedule_iteration_for_engagement(self):
    pass
