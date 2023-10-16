import bottle

app = bottle.Bottle()


data = {
    1: {'name': 'Item 1', 'description': 'Description for Item 1'},
    2: {'name': 'Item 2', 'description': 'Description for Item 2'},
    
}


@app.route('/items', method='GET')
def get_items():
    return {'items': data}


@app.route('/items/<id:int>', method='GET')
def get_item(id):
    if id in data:
        return data[id]
    else:
        bottle.response.status = 404
        return {'error': 'Item not found'}


@app.route('/items', method='POST')
def create_item():
    new_id = max(data.keys()) + 1
    item = bottle.request.json
    data[new_id] = item
    return {'id': new_id}


@app.route('/items/<id:int>', method='PUT')
def update_item(id):
    if id in data:
        item = bottle.request.json
        data[id] = item
        return {'message': 'Item updated'}
    else:
        bottle.response.status = 404
        return {'error': 'Item not found'}


@app.route('/items/<id:int>', method='DELETE')
def delete_item(id):
    if id in data:
        del data[id]
        return {'message': 'Item deleted'}
    else:
        bottle.response.status = 404
        return {'error': 'Item not found'}

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8000, debug=True)
