from .ToDoItem import db as ToDoItem


def init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/flask_todolist'
    ToDoItem.app = app
    ToDoItem.init_app(app)
    ToDoItem.create_all()
