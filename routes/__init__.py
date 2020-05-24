from .ToDoItem import to_do_items_blueprint


def init(app):
    app.register_blueprint(to_do_items_blueprint)
