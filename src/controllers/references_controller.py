from flask import Blueprint, render_template, redirect, request
from services.reference_service import reference_service
from services.user_service import user_service


ref_controller = Blueprint("ref", __name__)


@ref_controller.route('/references/')
def show_references():
    # change to accommodate all types of references, not just books

    user_id = user_service.get_id()

    references = reference_service.get_references(int(user_id))

    return render_template('references.html', user_id=user_id,
                           references=references)


@ref_controller.route('/references/add/', methods=['POST'])
def add_book():

    user_id = user_service.get_id()

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

    return redirect('/references/')
