from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/api/greet")
def greet():
    name = request.args.get("name", "mundo")
    return jsonify(message=f"Olá, {name}!")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)


# Apenas para teste do Gitleaks
GITHUB_TOKEN_FAKE = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD"