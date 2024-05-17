import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

from datetime import datetime

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/books", methods=["GET", "POST"])
@login_required
def add_books():
    favorite_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "favorite",
    )
    future_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "future",
    )
    if request.method == "POST":
        if not request.form.get("favorite_book"):
            return apology("Must provide a favorite book title", 400)
        else:
            favorite_book = request.form.get("favorite_book")
            db.execute(
                "INSERT INTO books (user_id, title, book_group) VALUES (?, ?, ?)",
                session["user_id"],
                favorite_book,
                "favorite",
            )
            favorite_books = db.execute(
                "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
                session["user_id"],
                "favorite",
            )
            return render_template(
                "books.html", favorite_books=favorite_books, future_books=future_books
            )
    return render_template(
        "books.html", favorite_books=favorite_books, future_books=future_books
    )


@app.route("/remove_favorite_book", methods=["POST"])
def remove_favorite_book():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM books WHERE id = ?", id)
    favorite_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "favorite",
    )
    future_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "future",
    )
    return render_template(
        "books.html", favorite_books=favorite_books, future_books=future_books
    )


@app.route("/future_books", methods=["POST"])
def add_future_books():
    if request.method == "POST":
        if not request.form.get("future_book"):
            return apology("Must provide a future book title", 400)
        else:
            future_book = request.form.get("future_book")
            db.execute(
                "INSERT INTO books (user_id, title, book_group) VALUES (?, ?, ?)",
                session["user_id"],
                future_book,
                "future",
            )
    future_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "future",
    )
    favorite_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "favorite",
    )
    return render_template(
        "books.html", favorite_books=favorite_books, future_books=future_books
    )


@app.route("/remove_future_book", methods=["POST"])
def remove_future_books():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM books WHERE id = ?", id)
    future_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "future",
    )
    favorite_books = db.execute(
        "SELECT id, title FROM books WHERE user_id = ? AND book_group = ?",
        session["user_id"],
        "favorite",
    )
    return render_template(
        "books.html", favorite_books=favorite_books, future_books=future_books
    )


@app.route("/movies", methods=["GET", "POST"])
@login_required
def add_movies():
    favorite_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "favorite",
    )
    future_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "future",
    )
    if request.method == "POST":
        if not request.form.get("favorite_movie"):
            return apology("Must provide a favorite movie title", 400)
        else:
            favorite_movie = request.form.get("favorite_movie")
            db.execute(
                "INSERT INTO movies (user_id, title, movie_group) VALUES (?, ?, ?)",
                session["user_id"],
                favorite_movie,
                "favorite",
            )
            favorite_movies = db.execute(
                "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
                session["user_id"],
                "favorite",
            )
            return render_template(
                "movies.html",
                favorite_movies=favorite_movies,
                future_movies=future_movies,
            )
    return render_template(
        "movies.html", favorite_movies=favorite_movies, future_movies=future_movies
    )


@app.route("/remove_favorite_movie", methods=["POST"])
def remove_favorite_movie():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM movies WHERE id = ?", id)
    favorite_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "favorite",
    )
    future_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "future",
    )
    return render_template(
        "movies.html", favorite_movies=favorite_movies, future_movies=future_movies
    )


@app.route("/future_movies", methods=["POST"])
def add_future_movies():
    if request.method == "POST":
        if not request.form.get("future_movie"):
            return apology("Must provide a future movie title", 400)
        else:
            future_movie = request.form.get("future_movie")
            db.execute(
                "INSERT INTO movies (user_id, title, movie_group) VALUES (?, ?, ?)",
                session["user_id"],
                future_movie,
                "future",
            )
    future_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "future",
    )
    favorite_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "favorite",
    )
    return render_template(
        "movies.html", favorite_movies=favorite_movies, future_movies=future_movies
    )


@app.route("/remove_future_movie", methods=["POST"])
def remove_future_movie():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM movies WHERE id = ?", id)
    future_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "future",
    )
    favorite_movies = db.execute(
        "SELECT id, title FROM movies WHERE user_id = ? AND movie_group = ?",
        session["user_id"],
        "favorite",
    )
    return render_template(
        "movies.html", favorite_movies=favorite_movies, future_movies=future_movies
    )


@app.route("/contact", methods=["GET", "POST"])
@login_required
def send_message():
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")
        name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        db.execute(
            "INSERT INTO contact (user_id, name, email, message) VALUES (?, ?, ?, ?)",
            session["user_id"],
            name[0]["username"],
            email,
            message,
        )
        return render_template("message_sent.html")
    return render_template("contact.html")


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)
        username = request.form.get("username")
        user = db.execute("SELECT * FROM users WHERE username = ?", [username])
        if user:
            return apology("This username is already taken", 400)
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology(
                "Neigther the password field nor the confirmation field can be empty",
                400,
            )
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)
        else:
            password = request.form.get("password")
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                generate_password_hash(password),
            )
            session["user_id"] = db.execute(
                "SELECT id FROM users WHERE username = ?", username
            )[0]["id"]
            return redirect("/")
    return render_template("register.html")
