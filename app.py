from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 초기 데이터 설정
members = {}
books = {}

# 홈 페이지
@app.route('/')
def home():
    return render_template('index.html', members=members, books=books)

# 멤버 추가
@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form.get('member_name')
    if member_name not in members:
        members[member_name] = []
    return redirect('/')

# 멤버 삭제
@app.route('/remove_member', methods=['POST'])
def remove_member():
    member_name = request.form.get('member_name')
    if member_name in members:
        del members[member_name]
    return redirect('/')

# 책 추가
@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form.get('book_title')
    if book_title not in books.values():
        books[len(books) + 1] = book_title
    return redirect('/')

# 책 삭제
@app.route('/remove_book', methods=['POST'])
def remove_book():
    book_id = int(request.form.get('book_id'))
    if book_id in books:
        del books[book_id]
    return redirect('/')

# 책 대출
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form.get('member_name')
    book_id = int(request.form.get('book_id'))
    if member_name in members and book_id in books:
        members[member_name].append(books[book_id])
        del books[book_id]
    return redirect('/')

# 책 반납
@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name in members and book_title in members[member_name]:
        books[len(books) + 1] = book_title
        members[member_name].remove(book_title)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
