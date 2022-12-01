from flask import Blueprint, render_template, redirect, request
from services.reference_service import reference_service


ref_controller = Blueprint("ref", __name__)


@ref_controller.route('/references/<user_id>')
def show_references(user_id):
    # change to accommodate all types of references, not just books
    references = reference_service.get_references(int(user_id))

    references_check = 0
    if references:
        references_check = 1

    return render_template('references.html', user_id=user_id,
                           references=references,
                           references_check=references_check)


@ref_controller.route('/references/add/<user_id>', methods=['POST'])
def add_book(user_id):
    authors = request.form.get('authors')
    title = request.form.get('title')
    year = request.form.get('year')
    publisher = request.form.get('publisher')
    print(user_id, authors, title, year, publisher)

    reference_service.create_book_reference(user_id=user_id,
                                            title=title,
                                            authors=authors,
                                            year=year,
                                            publisher=publisher)

    return redirect(f'/references/{user_id}')
