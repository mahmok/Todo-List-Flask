from flask import Blueprint
from controllers import ToDoItemsController

to_do_items_blueprint = Blueprint('to_do_items_blueprint', __name__)


@to_do_items_blueprint.route('/items')
def index():
    return ToDoItemsController.show_items()

@to_do_items_blueprint.route('/items/create')
def create_item():
    return ToDoItemsController.create_item()

@to_do_items_blueprint.route('/items/store', methods=["POST"])
def store_item():
    return ToDoItemsController.store_item()

@to_do_items_blueprint.route('/items/delete/<id>')
def delete_item(id):
    return ToDoItemsController.delete_item(id)

@to_do_items_blueprint.route('/items/edit/<id>')
def edit_item(id):
    return ToDoItemsController.edit_item(id)

@to_do_items_blueprint.route('/items/edit/<id>', methods = ["POST"])
def save_item(id):
    return ToDoItemsController.save_item(id)

@to_do_items_blueprint.route('/items/edit/<id>/status', methods = ["GET"])
def toggle_item_status(id):
    return ToDoItemsController.toggle_item_status(id)