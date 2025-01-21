from flask import Flask, request, render_template

app = Flask(__name__)

books = [
{"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
{"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}, 
{"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
{"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
{"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}]


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    author = request.args.get('author')

    # Recherche d'un livre via le nom de l'auteur
    for book in books:
        if book['author'] == author:
            return f'Titre : {book["title"]}, Auteur : {book["author"]}, AnnÃ©e : {book["year"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)