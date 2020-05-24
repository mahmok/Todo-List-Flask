from flask import render_template, url_for, redirect
from models.ToDoItem import ToDoItem, db
from flask import request

def show_items():
    items = ToDoItem.query.all()
    return render_template("all_items.html", items=items)

def create_item():
    return render_template("create.html")

def store_item():
    item = ToDoItem(title=request.form.get("title"), description=request.form.get("description"))
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('to_do_items_blueprint.index'))

def delete_item(id):
    ToDoItem.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('to_do_items_blueprint.index'))

def edit_item(id):
    item = ToDoItem.query.filter_by(id=id).first()
    return render_template("edit.html", item=item)

def save_item(id):
    item = ToDoItem.query.filter_by(id=id).first()
    item.title = request.form.get("title")
    item.description = request.form.get("description")
    db.session.commit()
    return render_template("edit.html", item=item)


def toggle_item_status(id):
    item = ToDoItem.query.filter_by(id=id).first()
    if item.status == "pending":
        item.status = "completed"
    else:
        item.status = "pending"
    db.session.commit()
    return redirect(url_for('to_do_items_blueprint.index'))