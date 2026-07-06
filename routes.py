from flask import Blueprint, request, jsonify
from services import create_short_url

url_bp = Blueprint("url", __name__)

@url_bp.route("/shorten", methods=["POST"])
def shorten_url():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({
            "message": "URL is required"
        }), 400

    url = create_short_url(data["url"])

    return jsonify({
        "original_url": url.original_url,
        "short_code": url.short_code
    }), 201