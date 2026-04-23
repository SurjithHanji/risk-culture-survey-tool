from flask import Flask, request, jsonify
from services.input_sanitizer import validate_request

app = Flask(__name__)

# 🔐 Middleware (runs before every request)
@app.before_request
def check_input():
    if request.method in ["POST", "PUT"]:
        error = validate_request()
        if error:
            return error


# 🏠 Home route (to avoid 404)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Service is running successfully 🚀"
    })


# 🧪 Test route (for testing sanitisation)
@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    return jsonify({
        "message": "Request passed successfully",
        "cleaned_data": data
    })


# ▶️ Run the app
if __name__ == "__main__":
    app.run(debug=True)