# Anomoly Detector

Currently this app has functionality to run a jupyter notebook in a docker container with a bind mount to create and run notebooks in server.

## Techniques employed

- Software architecture and design
- A mix of data science and data engineering
- Microservices: FastAPI
- Anomaly detection: Isolation forest model, scikit-learn and Plotly
- Data analysis and visualization: seaborn
- Monitoring and metrics: Prometheus, prometheus_client, and Grafana
- Dockerizing: Docker, Docker-Compose

## To run locally

- `docker compose up`
- Navigate to localhost:4001
  - password = password
