from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/profile/<username>/')
def profile(username):
	return render_template('profile.html',username=username,isActive=False)

@app.route('/books')

def book():
	books=[{'name':'The Alchemist','author':'Paulo Coelho','img':'https://rukminim2.flixcart.com/image/850/1000/xif0q/book/x/p/j/-original-imagqtdtbkdccy4x.jpeg?q=90&crop=false'},
	{'name':'Pathummayude Aadu','author':'Vaikom Muhammad Basheer','img':'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQWmMdCPCWZQpLpbnkWtEyUM3MFEGw1nm1K3WEPz8KRp3bsn-7H'},
	{'name':'Bhoomiyude Avakasikal','author':'Vaikom Muhammad Basheer','img':'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1479051386i/17373495.jpg'}]
	return render_template('book.html',books=books)

app.run(debug=True)