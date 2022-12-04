from flask import Blueprint, render_template, redirect, request
from services.reference_service import reference_service
from services.user_service import user_service


ref_controller = Blueprint("ref", __name__)


@ref_controller.route('/references/')
def show_references():
    user_id = user_service.get_id()

    books = reference_service.get_book_references(int(user_id))
    articles = reference_service.get_article_references(int(user_id))
    inproceedings = reference_service.get_inproceeding_references(int(user_id))

    return render_template('references.html', user_id=user_id, books=books,
                                            articles=articles, inproceedings=inproceedings)

@ref_controller.route('/references/book/', methods=['POST'])
def add_book():
    user_id = user_service.get_id()

    authors = request.form.get('authors')
    title = request.form.get('title')
    year = request.form.get('year')
    publisher = request.form.get('publisher')

    reference_service.create_book_reference(user_id=user_id, authors=authors, title=title,
                                            year=year, publisher=publisher)

    return redirect('/references/')

@ref_controller.route('/references/article/', methods=['POST'])
def add_article():
    user_id = user_service.get_id()

    authors = request.form.get('authors')
    title = request.form.get('title')
    journal = request.form.get('journal')
    year = request.form.get('year')
    volume = request.form.get('volume')
    pages = request.form.get('pages')

    reference_service.create_article_reference(user_id=user_id, authors=authors, title=title,
                                               journal=journal, year=year, volume=volume,
                                               pages=pages)

    return redirect('/references/')

@ref_controller.route('/references/inproceeding/', methods=['POST'])
def add_inproceeding():
    user_id = user_service.get_id()

    authors = request.form.get('authors')
    title = request.form.get('title')
    year = request.form.get('year')
    booktitle = request.form.get('booktitle')

    reference_service.create_inproceeding_reference(user_id=user_id, authors=authors, title=title,
                                                    year=year, booktitle=booktitle)

    return redirect('/references/')
