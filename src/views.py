from flask import Blueprint, redirect, url_for, render_template

from .forms import BookForm
from .models import Book


home = Blueprint('home', __name__)

books = []


@home.route('/')
def index():
    return render_template('index.html', books=books)


@home.route('/book', methods=['GET', 'POST'])
def book():
    form = BookForm()
    if form.validate_on_submit():
        books.append(Book(author=form.author.data, title=form.title.data))
        return redirect(url_for('home.index'))
    return render_template('book.html', form=form)
