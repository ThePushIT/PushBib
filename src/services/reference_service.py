import os
from flask_babel import lazy_gettext
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from repositories.reference_repository import reference_repository as default_reference_repository


class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    # syötteiden oikeellisuuden tarkistaminen
    def create_book_reference(self, user_id, authors, title, year, publisher):
        authors_str = self.create_author_str(authors)
        print(authors_str)
        self._reference_repository.insert_book_reference(
            user_id, authors_str, title, year, publisher)

    def create_article_reference(self, user_id, authors, title, journal, year, volume, pages):
        authors_str = self.create_author_str(authors)
        self._reference_repository.insert_article_reference(
            user_id, authors_str, title, journal, year, volume, pages)

    def create_inproceeding_reference(self, user_id, authors, title, year, booktitle):
        authors_str = self.create_author_str(authors)
        self._reference_repository.insert_inproceeding_reference(
            user_id, authors_str, title, year, booktitle)

    def create_misc_reference(self, user_id, authors, title, howpublished, year, note):
        authors_str = self.create_author_str(authors)
        self._reference_repository.insert_misc_reference(
            user_id, authors_str, title, howpublished, year, note)

    def get_book_references(self, user_id):
        return self._reference_repository.fetch_book_references(user_id)

    def convert_books_into_dictionaries(self, book_tuples):
        print('book tuples', book_tuples)
        book_dicts = []
        for book in book_tuples:
            book_dict = {
                "type": "book",
                "id": book[0],
                lazy_gettext("Author(s)"): book[1],
                lazy_gettext("Title"): book[2],
                lazy_gettext("Year"): book[3],
                lazy_gettext("Publisher"): book[4]
            }

            book_dicts.append(book_dict)

        return book_dicts

    def get_article_references(self, user_id):
        return self._reference_repository.fetch_article_references(user_id)

    def convert_articles_into_dictionaries(self, article_tuples):
        article_dicts = []
        for article in article_tuples:
            article_dict = {
                "type": "article",
                "id": article[0],
                lazy_gettext("Author(s)"): article[1],
                lazy_gettext("Title"): article[2],
                lazy_gettext("Journal"): article[3],
                lazy_gettext("Year"): article[4],
                lazy_gettext("Volume"): article[5],
                lazy_gettext("Pages"): article[6]
            }

            article_dicts.append(article_dict)

        return article_dicts

    def get_inproceeding_references(self, user_id):
        return self._reference_repository.fetch_inproceeding_references(user_id)

    def convert_inproceedings_into_dictionaries(self, inproceeding_tuples):
        inproceeding_dicts = []
        for inproceeding in inproceeding_tuples:
            inproceeding_dict = {
                "type": "inproceeding",
                "id": inproceeding[0],
                lazy_gettext("Author(s)"): inproceeding[1],
                lazy_gettext("Title"): inproceeding[2],
                lazy_gettext("Year"): inproceeding[3],
                lazy_gettext("Booktitle"): inproceeding[4]
            }

            inproceeding_dicts.append(inproceeding_dict)

        return inproceeding_dicts

    def get_misc_references(self, user_id):
        return self._reference_repository.fetch_misc_references(user_id)

    def convert_misc_into_dictionaries(self, misc_tuples):
        misc_dicts = []
        for misc in misc_tuples:
            misc_dict = {
                "type": "misc",
                "id": misc[0],
                lazy_gettext("Author(s)"): misc[1],
                lazy_gettext("Title"): misc[2],
                lazy_gettext("Howpublished"): misc[3],
                lazy_gettext("Year"): misc[4],
                lazy_gettext("Note"): misc[5]
            }

            misc_dicts.append(misc_dict)

        return misc_dicts

    def get_all_references_by_user_id(self, user_id):
        books = self.get_book_references(user_id)
        books = self.convert_books_into_dictionaries(books)
        articles = self.get_article_references(user_id)
        articles = self.convert_articles_into_dictionaries(articles)
        inproceedings = self.get_inproceeding_references(user_id)
        inproceedings = self.convert_inproceedings_into_dictionaries(inproceedings)
        misc = self.get_misc_references(user_id)
        misc = self.convert_misc_into_dictionaries(misc)

        references = books + articles + inproceedings + misc

        return references

    def sort_references_alphabetically_by_author(self, references):
        references.sort(key = lambda reference: reference[lazy_gettext("Author(s)")])

        return references

    def delete_reference(self, reference_id, reference_type):
        if reference_type == "book":
            self._reference_repository.delete_book_reference(reference_id)
        if reference_type == "article":
            self._reference_repository.delete_article_reference(reference_id)
        if reference_type == "inproceeding":
            self._reference_repository.delete_inproceeding_reference(reference_id)
        if reference_type == "misc":
            self._reference_repository.delete_misc_reference(reference_id)


    def delete_all_references(self):
        return self._reference_repository.delete_all_references()

    def convert_all_references_to_bibtex(self, user_id):
        id_number = 1

        bib_db = BibDatabase()
        books = self.get_book_references(user_id)
        self._add_books_to_bib_database(books, bib_db, id_number)

        articles = self.get_article_references(user_id)
        self._add_articles_to_bib_database(articles, bib_db, id_number)

        inproceedings = self.get_inproceeding_references(user_id)
        self._add_inproceedings_to_bib_database(inproceedings, bib_db, id_number)

        misc = self.get_misc_references(user_id)
        self._add_misc_to_bib_database(misc, bib_db, id_number)

        return bib_db

    def create_bibtex_file(self, user_id):

        bib_db = self.convert_all_references_to_bibtex(user_id)

        print(bib_db)

        try:
            os.mkdir(os.path.join(os.getcwd(), "user_files"))
        except FileExistsError:
            pass

        file_path = os.path.join(os.getcwd(),
                                "user_files",
                                f"references_{user_id}.bib")

        writer = BibTexWriter()
        writer.order_entries_by = ("author", "year")
        writer.display_order = ("author", "howpublished", "title", "journal", \
                                "year", "volume", "pages")
        with open(file_path, "w+", encoding="utf-8") as bibfile:
            bibfile.write(writer.write(bib_db))

        return file_path

    @staticmethod
    def replace_special_characters(text):
        text = text.replace("&", r"\&")
        text = text.replace("_", r"\_")
        text = text.replace("%", r"\%")
        text = text.replace("#", r"\#")

        return text

    def create_author_str(self, authors):
        authors.sort()
        authors_str = authors[0]
        for author in authors[1:]:
            authors_str += ' and ' + author
        return authors_str

    def _add_books_to_bib_database(self,
                                        books : list,
                                        bib_db : BibDatabase,
                                        id_number : int):
        for book in books:
            bib_db.entries.append(
                {"title": ReferenceService.replace_special_characters(book.title),
                "author": book.authors,
                "year": str(book.year),
                "publisher": book.publisher,
                "ID": f"b{id_number}",
                "ENTRYTYPE": "book"
                }
            )
            id_number+=1

    def _add_articles_to_bib_database(self,
                                        articles : list,
                                        bib_db : BibDatabase,
                                        id_number: int):
        for article in articles:
            bib_db.entries.append(
                {"title": ReferenceService.replace_special_characters(article.title),
                "author": article.authors,
                "year": str(article.year),
                "journal": ReferenceService.replace_special_characters(article.journal),
                "volume": str(article.volume),
                "pages": article.pages,
                "ID": f"a{id_number}",
                "ENTRYTYPE": "article"}
            )
            id_number+=1

    def _add_inproceedings_to_bib_database(self,
                                            inproceedings : list,
                                            bib_db : BibDatabase,
                                            id_number : int):
        for inproceeding in inproceedings:
            bib_db.entries.append(
                {"title": ReferenceService.replace_special_characters(inproceeding.title),
                "author": inproceeding.authors,
                "year": str(inproceeding.year),
                "booktitle": ReferenceService.replace_special_characters(inproceeding.booktitle),
                "ID": f"ip{id_number}",
                "ENTRYTYPE": "InProceedings"
                }
            )
            id_number+=1

    def _add_misc_to_bib_database(self,
                                            misc : list,
                                            bib_db : BibDatabase,
                                            id_number : int):
        for i in misc:
            bib_db.entries.append(
                {"title": ReferenceService.replace_special_characters(i.title),
                "author": i.authors,
                "howpublished": ReferenceService.replace_special_characters(i.howpublished),
                "year": str(i.year),
                "note": ReferenceService.replace_special_characters(i.note),
                "ID": f"m{id_number}",
                "ENTRYTYPE": "misc"
                }
            )
            id_number+=1


reference_service = ReferenceService()
