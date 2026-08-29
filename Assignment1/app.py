from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
# The application starts with no books.
books = []


# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book

    return None


# ==================================================
# 1. GET ALL BOOKS
# ==================================================

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200


# ==================================================
# 2. GET A SINGLE BOOK
# ==================================================

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):

    book = find_book(book_id)

    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    return jsonify(book), 200


# ==================================================
# 3. CREATE A BOOK
# ==================================================

@app.route("/books", methods=["POST"])
def create_book():

    data = request.get_json()

    if data is None:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    # Check required fields
    if "title" not in data:
        return jsonify({
            "error": "title is required"
        }), 400

    if "author" not in data:
        return jsonify({
            "error": "author is required"
        }), 400

    if "genre" not in data:
        return jsonify({
            "error": "genre is required"
        }), 400

    # Generate a new ID
    if len(books) == 0:
        new_id = 1
    else:
        new_id = max(book["id"] for book in books) + 1

    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
        "available": True
    }

    books.append(new_book)

    return jsonify(new_book), 201


# ==================================================
# 4. UPDATE A BOOK
# ==================================================

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = find_book(book_id)

    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    data = request.get_json()
    book["title"] = data["title"]
    book["author"] = data["author"]
    book["genre"] = data["genre"]

    return jsonify(book), 200


# ==================================================
# 5. DELETE A BOOK
# ==================================================

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = find_book(book_id)

    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    books.remove(book)
    return "", 204


# ==================================================
# START SERVER
# ==================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
