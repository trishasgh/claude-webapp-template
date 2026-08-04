# UCSD Citizen App

A citizen-developed web application running on the UC San Diego TritonAI platform.

- **Stack:** Python / FastAPI served by uvicorn on port 8000
- **Container:** `python:3.13-slim`, non-root `appuser`
- **Health check:** `GET /api/health`
- **Frontend:** static HTML/CSS/JS + JWT auth (sqlite-backed)

Pushing to `main` builds the container in GitHub Actions and publishes it to GHCR.
Deployment to the campus Kubernetes platform is handled by the TritonAI platform team.
