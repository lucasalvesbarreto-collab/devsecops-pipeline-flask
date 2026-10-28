from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/")
def health() -> tuple[dict[str, str], int]:
    return jsonify(status="healthy", service="devsecops-pipeline-flask"), 200


@api.get("/health")
def health_alias() -> tuple[dict[str, str], int]:
    return jsonify(status="healthy"), 200
