from flask import Flask, request, jsonify

app = Flask(__name__)

database = {
    "users": [
        {
            "avatar": "https://reqres.in/img/faces/1-image.jpg",
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "id": 1,
            "last_name": "Bluth"
        },
        {
            "avatar": "https://reqres.in/img/faces/2-image.jpg",
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "id": 2,
            "last_name": "Weaver"
        },
        {
            "avatar": "https://reqres.in/img/faces/3-image.jpg",
            "email": "emma.wong@reqres.in",
            "first_name": "Emma",
            "id": 3,
            "last_name": "Wong"
        },
        {
            "avatar": "https://reqres.in/img/faces/4-image.jpg",
            "email": "eve.holt@reqres.in",
            "first_name": "Eve",
            "id": 4,
            "last_name": "Holt"
        },
        {
            "avatar": "https://reqres.in/img/faces/5-image.jpg",
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "id": 5,
            "last_name": "Morris"
        },
        {
            "avatar": "https://reqres.in/img/faces/6-image.jpg",
            "email": "tracey.ramos@reqres.in",
            "first_name": "Tracey",
            "id": 6,
            "last_name": "Ramos"
        },
        {
            "avatar": "https://reqres.in/img/faces/7-image.jpg",
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "id": 7,
            "last_name": "Lawson"
        },
        {
            "avatar": "https://reqres.in/img/faces/8-image.jpg",
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "id": 8,
            "last_name": "Ferguson"
        },
        {
            "avatar": "https://reqres.in/img/faces/9-image.jpg",
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "id": 9,
            "last_name": "Funke"
        },
        {
            "avatar": "https://reqres.in/img/faces/10-image.jpg",
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "id": 10,
            "last_name": "Fields"
        },
        {
            "avatar": "https://reqres.in/img/faces/11-image.jpg",
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "id": 11,
            "last_name": "Edwards"
        },
        {
            "avatar": "https://reqres.in/img/faces/12-image.jpg",
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "id": 12,
            "last_name": "Howell"
        }
    ]
}


@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 6))
    except Exception:
        return jsonify({"error": "Invalid page or per_page parameter"}), 400

    total = len(database['users'])

    # 计算正确的起始和结束索引
    start_idx = (page - 1) * per_page
    end_idx = min(start_idx + per_page, total)

    return jsonify({
        "page": page,
        "per_page": per_page,
        "total": total,
        # 1 if total % per_page else 0
        # 等价于
        # if total % per_page:
        #     result = 1
        # else:
        #     result = 0
        "total_pages": (total // per_page) + (1 if total % per_page else 0),
        # 前开后闭
        "data": database['users'][start_idx:end_idx]
    })


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in database['users'] if u['id'] == user_id), None)
    if user:
        return jsonify({"data": user})
    return jsonify({"error": "User not found"}), 404


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_id = max(user['id'] for user in database['users']) + 1
    new_user = {
        "id": new_id,
        "email": data.get("email"),
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "avatar": "https://reqres.in/img/faces/{}-image.jpg".format(new_id)
    }
    database['users'].append(new_user)
    return jsonify(new_user), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = next((u for u in database['users'] if u['id'] == user_id), None)
    if user:
        user.update(data)
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global database
    database['users'] = [u for u in database['users'] if u['id'] != user_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
