from flask import Flask, jsonify, request

app = Flask(__name__)


## initial data in my to do list
items = [
    {'id': 1, 'title': 'Buy groceries', 'description': "the Groceries are bought"},
    {'id': 2, 'title': 'Clean the house', 'description': "The house is cleaned"},
    {'id': 3, 'title': 'Wash the car', 'description': "the car is wased"}
]


@app.route("/")
def home():
    return "Welcome to the To-Do List API!"


# get retrive all the items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


## get: Retrireve a specific  item by id
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next(( item for item in items if item ["id"]==item_id),None)
    if item is None:
        return jsonify({"error": "Item not found"})
    return jsonify(item)



## Post: create a new task
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "title" in request.json:
        return jsonify({"error": "Item not found"})
    new_item = {
    "id": items[-1]['id'] + 1 if items else 1,
    "title": request.json["title"],
    "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)



# Put: update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next(( item for item in items if item ["id"]==item_id),None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['title'] = request.json.get('title', item['title'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)


# Delete: delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item ["id"] != item_id]
    return jsonify({"result": "item deleted"})


if __name__ == '__main__':
    app.run(debug=True)