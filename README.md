# devsecops-pipeline-flask

API Flask minimalista com pipeline DevSecOps no GitHub Actions.

## Executar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pytest --cov=app tests/
python -m flask --app app:create_app run --port 8080
```

## Docker

```bash
docker build -t devsecops-pipeline-flask .
docker run --rm -p 8080:8080 devsecops-pipeline-flask
```

## Pipeline

O workflow executa testes, cobertura, análise estática, auditoria de dependências, Docker build, scan de imagem com Trivy e análise de código com CodeQL.
