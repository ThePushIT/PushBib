from flask import Blueprint, render_template, redirect, request, send_file
from services.reference_service import reference_service
from services.user_service import user_service

ref_controller = Blueprint("ref", __name__)


@ref_controller.route("/references/")
def show_references():
    page = "references"
    user_id = user_service.get_id()
    if user_id == 0:
        return redirect("/")

    references = reference_service.get_all_references_by_user_id(user_id)
    references = reference_service.sort_references_alphabetically_by_author(references)

    return render_template("references.html", user_id=user_id, references=references, page=page)

@ref_controller.route("/references/book/", methods=["POST"])
def add_book():
    print("tultiin bookin post metodin controllointiin")
    user_id = user_service.get_id()
    user_service.check_csrf(request.form["csrf_token"])

    authors = []

    form = request.form
    for key in form.keys():
        if "author" in key:
            value = form.get(key)
            if len(value) > 0:
                authors.append(value)

    print(authors)
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")

    reference_service.create_book_reference(user_id=user_id, authors=authors,
                                            title=title, year=year,publisher=publisher)

    return redirect("/references/")

@ref_controller.route("/references/article/", methods=["POST"])
def add_article():
    user_id = user_service.get_id()
    user_service.check_csrf(request.form["csrf_token"])

    authors = []

    form = request.form
    for key in form.keys():
        if "author" in key:
            value = form.get(key)
            if len(value) > 0:
                authors.append(value)

    title = request.form.get("title")
    journal = request.form.get("journal")
    year = request.form.get("year")
    volume = request.form.get("volume")
    pages = request.form.get("pages")

    reference_service.create_article_reference(user_id=user_id, authors=authors, title=title,
                                               journal=journal, year=year, volume=volume,
                                               pages=pages)

    return redirect("/references/")

@ref_controller.route("/references/inproceeding/", methods=["POST"])
def add_inproceeding():
    user_id = user_service.get_id()
    user_service.check_csrf(request.form["csrf_token"])

    authors = []
    form = request.form
    for key in form.keys():
        if "author" in key:
            value = form.get(key)
            if len(value) > 0:
                authors.append(value)

    title = request.form.get("title")
    year = request.form.get("year")
    booktitle = request.form.get("booktitle")

    reference_service.create_inproceeding_reference(user_id=user_id, authors=authors,
                                                    title=title, year=year, booktitle=booktitle)

    return redirect("/references/")

@ref_controller.route("/references/misc/", methods=["POST"])
def add_misc():
    user_id = user_service.get_id()
    user_service.check_csrf(request.form["csrf_token"])

    authors = []
    form = request.form
    for key in form.keys():
        if "author" in key:
            value = form.get(key)
            if len(value) > 0:
                authors.append(value)

    title = request.form.get("title")
    howpublished = request.form.get("howpublished")
    year = request.form.get("year")
    note = request.form.get("note")

    reference_service.create_misc_reference(user_id=user_id, authors=authors,
                                            title=title, howpublished=howpublished,
                                            year=year, note=note)

    return redirect("/references/")

@ref_controller.route("/references/delete", methods=["POST"])
def delete_reference():
    user_service.check_csrf(request.form["csrf_token"])

    reference_id = request.form["reference_id"].strip()
    reference_type = request.form["reference_type"].strip()
    reference_service.delete_reference(reference_id, reference_type)

    return redirect("/references")

@ref_controller.route("/references/download")
def download_references():
    user_id = user_service.get_id()

    if user_id == 0:
        return redirect("/")

    file_path = reference_service.create_bibtex_file(user_id)

    return send_file(file_path, as_attachment=True, download_name="references.bib")
