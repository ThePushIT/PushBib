from datetime import date
import os
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from repositories.reference_repository import reference_repository as default_reference_repository


class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    # syötteiden oikeellisuuden tarkistaminen
    def create_book_reference(self, user_id, authors, title, year, publisher):
        self._reference_repository.insert_book_reference(
            user_id, authors, title, year, publisher)

    def create_article_reference(self, user_id, authors, title, journal, year, volume, pages):
        self._reference_repository.insert_article_reference(
            user_id, authors, title, journal, year, volume, pages)

    def create_inproceeding_reference(self, user_id, authors, title, year, booktitle):
        self._reference_repository.insert_inproceeding_reference(
            user_id, authors, title, year, booktitle)

    def get_book_references(self, user_id):
        return self._reference_repository.fetch_book_references(user_id)

    def get_article_references(self, user_id):
        return self._reference_repository.fetch_article_references(user_id)

    def get_inproceeding_references(self, user_id):
        return self._reference_repository.fetch_inproceeding_references(user_id)

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

        return bib_db

        #Try to make the directory where the server will save all .bib files.
    #    try:
     #       os.mkdir(os.path.join(os.getcwd(), "user_files"))
      #  except FileExistsError:
       #     pass

        #file_path = os.path.join(os.getcwd(),
         #                       "user_files",
          #                      f"references_{user_id}_{date.today()}.bib")

        #writer = BibTexWriter()
  #      with open(file_path, "w+", encoding="utf-8") as bibfile:
   #         bibfile.write(writer.write(bib_db))
#
 #       return file_path

    def create_bibtex_file(self, user_id):

        bib_db = self.convert_all_references_to_bibtex(user_id)

        print(bib_db)

        try:
            os.mkdir(os.path.join(os.getcwd(), "user_files"))
        except FileExistsError:
            pass

        file_path = os.path.join(os.getcwd(),
                                "user_files",
                                f"references_{user_id}_{date.today()}.bib")

        writer = BibTexWriter()
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


reference_service = ReferenceService()
