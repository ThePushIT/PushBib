from flask import Blueprint, render_template, redirect, request

ref_controller = Blueprint("ref", __name__)

@ref_controller.route('/references/<id>')
def show_references(id):
    user_id = id
    # find the user in case
    # find all the references by this user
    # give as a parameter for the template

    #references = reference_service.get_all_references(user_id)

    return render_template('references.html', user = user_id)

@ref_controller.route('/references/add/<id>', methods = ['POST'])
def add_reference(id):
    user_id = id
    name = request.form.get('name')
    authors = request.form.get('authors')
    year = request.form.get('year')
    print(name, authors, year, user_id)

    return redirect(f'/references/{id}')