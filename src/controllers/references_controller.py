from flask import Blueprint, render_template, redirect, request
from services.reference_service import reference_service


ref_controller = Blueprint("ref", __name__)

@ref_controller.route('/references/<user_id>', methods=['GET'])
def show_references(user_id):
    # change to accommodate all types of references, not just books
    user = user_id
    references = reference_service.get_references(user_id)

    return render_template('references.html', user=user, 
                                            references=references)

@ref_controller.route('/references/add/<user_id>', methods=['POST'])
def add_book(user_id):
    print(user_id)
    user = user_id
    authors = request.form.get('authors')
    title = request.form.get('title')
    year = request.form.get('year')
    publisher = request.form.get('publisher')
    print(title, authors, year, user, publisher)

    reference_service.create_book_reference(user=user,
                                        title=title,
                                        authors=authors,
                                        year=year,
                                        publisher=publisher)

    return redirect(f'/references/{user}')
