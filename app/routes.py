# from flask import Blueprint

# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello World!"
#     return my_beautiful_response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     my_dictionary = {
#     "name": "Angela Fan",
#     "message": "I like turtles.",
#     "hobbies": ["Fishing", "Swimming", "Watching Non-Reality Shows"]
#     }
#     return my_dictionary

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

# from flask import Blueprint, jsonify

# class Book: 
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

# books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)


# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book_id = int(book_id)
#     for book in books:
#         if book.id == book_id:
#             return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }

from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix = "/books")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
        if request.method == "GET":
                books = Book.query.all()
                books_response = []
                for book in books:
                        books_response.append({
                                "id": book.id,
                                "title": book.title,
                                "description": book.description
                        })
                return jsonify(books_response)

        elif request.method == "POST":
                request_body = request.get_json()
                new_book = Book(title=request_body["title"],
                                description=request_body["description"])
                
                db.session.add(new_book)
                db.session.commit()

                return make_response(f"Book {new_book.title} successfully created", 201)


@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
        book = Book.query.get(book_id)

        if request.method == "GET":
                return {
                        "id": book.id,
                        "title": book.title,
                        "description": book.description
                }
        elif request.method == "PUT":
                updated_body = request.get_json()

                book.title = updated_body["title"]
                book.description = updated_body["description"]
                # updated_book = Book(title = updated_body["title"],
                #                 description = updated_body["desciption"])
                db.session.commit()
                return make_response(f"Book #{book_id} successfully updated.")
        
        elif request.method == "DELETE":
                
                db.session.delete(book)
                db.session.commit()
                return make_response(f"Book #{book_id} successfully deleted.")