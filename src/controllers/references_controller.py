from flask import Blueprint

ref_controller = Blueprint("ref", __name__)

@ref_controller.route('/references/')
def show_references():
    # find the user in case
    # find all the references by this user
    # put to the template

    # on top of the template a form for adding a new reference

    #references = reference_service.get_all_references(user_id)

    return "Welcome to references"
