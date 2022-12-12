from flask import Blueprint, render_template, redirect, request, send_file
from services.reference_service import reference_service
from services.user_service import user_service
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SelectField, SubmitField
from wtforms.validators import DataRequired


class AddNewReferenceForm(FlaskForm):
    type = SelectField('Type', choices=[('book', 'book'),
                                        ('article', 'article'),
                                        ('inproceeding', 'inproceeding')])
    title = StringField('Title', validators = [DataRequired()])
    year = StringField('Year', validators=[DataRequired()])

    #csrf_token = user_service.get_csrf()
    #print(csrf_token)
    # common to all
    #submit = SubmitField('Add reference')

class BookForm(AddNewReferenceForm):
    #book specific
    authors_book = FieldList(StringField('Author Name', validators=[DataRequired()]), min_entries=1, max_entries=6, label='Authors')
    publisher = StringField('Publisher', validators=[DataRequired()])

class ArticleForm(AddNewReferenceForm):
    # article specific
    authors_article = FieldList(StringField('Author Name', validators=[DataRequired()]), min_entries=1, max_entries=6, label='Authors')
    journal = StringField('Journal', validators=[DataRequired()])
    volume = StringField('Volume', validators=[DataRequired()])
    pages = StringField('Pages', validators=[DataRequired()])

class InproceedingForm(AddNewReferenceForm):
    # inproceeding specific
    authors_inproceeding = FieldList(StringField('Author Name', validators=[DataRequired()]), min_entries=1, max_entries=6, label='Authors')
    booktitle = StringField('Booktitle', validators=[DataRequired()])




ref_controller = Blueprint("ref", __name__)


@ref_controller.route('/references/', methods = ['GET', 'POST'])
def show_references():
    
    user_id = user_service.get_id()
    if user_id == 0:
        return redirect('/')

   # bookForm = BookForm()
   # articleForm = ArticleForm()
   # inproceedingForm = InproceedingForm()

   # if addNewReferenceForm.validate_on_submit():
    #    ref_type = addNewReferenceForm.type.data
    #    authors = addNewReferenceForm.authors.entries
     #   author_list = []
      #  for author in authors:
       #     author_list.append(author)

        #title = addNewReferenceForm.title.data
        #year = addNewReferenceForm.year.data

        #if ref_type == 'book':
         #   publisher = addNewReferenceForm.publisher.data
          #  if len(publisher) == 0:
           #     print('publisher on none')

    books = reference_service.get_book_references(user_id)
    articles = reference_service.get_article_references(user_id)
    inproceedings = reference_service.get_inproceeding_references(user_id)

    return render_template('references.html', user_id=user_id, 
                                            books=books,
                                            articles=articles,
                                            inproceedings=inproceedings,)

@ref_controller.route('/references/book/', methods=['POST'])
def add_book():

    print('tultiin bookin post metodin controllointiin')
    user_id = user_service.get_id()
    #user_service.check_csrf(request.form["csrf_token"])

    # TODO
    # csrf token toimimaan
    # authorien hakeminen toimimaan

    bookForm = BookForm()

    if bookForm.validate_on_submit():
        print('bookissa validate on submittissa')
        authors = bookForm.authors_book.entries
        print(authors)

    authors = request.form.get('authors_book')
    title = request.form.get('title')
    year = request.form.get('year')
    publisher = request.form.get('publisher')

    reference_service.create_book_reference(user_id=user_id, authors=authors,
                                            title=title, year=year,publisher=publisher)

    return redirect('/references/')

@ref_controller.route('/references/article/', methods=['POST'])
def add_article():
    user_id = user_service.get_id()
    #user_service.check_csrf(request.form["csrf_token"])

    authors = request.form.get('authors_article')
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
    #user_service.check_csrf(request.form["csrf_token"])

    authors = request.form.get('authors_inproceeding')
    title = request.form.get('title')
    year = request.form.get('year')
    booktitle = request.form.get('booktitle')

    reference_service.create_inproceeding_reference(user_id=user_id, authors=authors,
                                                    title=title, year=year, booktitle=booktitle)

    return redirect('/references/')

@ref_controller.route('/references/download')
def download_references():
    user_id = user_service.get_id()

    if user_id == 0:
        return redirect('/')

    file_path = reference_service.create_bibtex_file(user_id)

    return send_file(file_path, as_attachment=True, download_name="references.bib")
