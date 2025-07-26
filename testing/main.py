from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

# GET = request data from specific resource
# POST = create a resource
# PUT = update a resource
# DELETE = remove a resource

# We are sending a GET request
# http://127.0.0.1:5000/get_user/123?extra=%22hello%22

# path parameter = dynamic value u can pass in path of url
@app.route('/get_user/<user_id>')
def get_user(user_id):
    # Create dictionary and then JSONify it. Also return status code.
    user_data = {
        "user_id": user_id, 
        "name": "John Doe", 
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200



# A POST request
@app.route('/create_user', methods=['POST'])
def create_user():
    # if request.method == 'POST':
    data = request.get_json()
    
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)