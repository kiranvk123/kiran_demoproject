# Kiran Demo Project
Simple Flask app deployed via Docker, Jenkins, and Helm to Kubernetes.

## Project Structure
- app.py → Flask application
- requirements.txt → Python dependencies
- Dockerfile → Container build instructions
- helm-chart/ → Helm templates for Kubernetes deployment
- Jenkinsfile → CI/CD pipeline definition

## How to Run
1. Build Docker image:
   ```bash
   docker build -t kiranvk123/kiran-demo .

