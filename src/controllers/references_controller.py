from flask import Blueprint, render_template, redirect, request
from services.reference_service import reference_service

ref_controller = Blueprint("ref", __name__)

@ref_controller.route('/references/<user_id>')
def show_references(user_id):
    user = user_id
    # find the user in case
    # find all the references by this user
    # give as a parameter for the template

    #references = reference_service.get_all_references(user_id)

    return render_template('references.html', user = user)

@ref_controller.route('/references/add/<user_id>', methods = ['POST'])
def add_reference(user_id):
    print(user_id)
    user = user_id
    name = request.form.get('name')
    authors = request.form.get('authors')
    year = request.form.get('year')
    print(name, authors, year, user)

    reference_service.create_reference(user_id = user,
                                        name = name,
                                        authors = authors,
                                        year = year)

    return redirect(f'/references/{user}')
