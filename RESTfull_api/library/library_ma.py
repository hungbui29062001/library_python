from .extension import ma

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name', 'email')

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class BooksSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ('id', 'students_id', 'books_id', 'borrow_date', 'return_date')

class TokenBlockListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'jti', 'created_at')