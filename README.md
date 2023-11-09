# Anomoly Detector

Sample end-to-end data product that employs a machine learning model for anomaly detection, web services, and monitoring tools to find those unusual cases lingering in a platform

This sample data platform consists of three main components: a service that serves the anomaly detection model, the monitoring platform Prometheus, and Grafana. The anomaly detector is an Isolation forest model trained with a curated and real dataset located at `/jupyter/test.csv && /jupyter/train.csv`. As part of the model development, we visualize the anomalous decision boundary to understand its decisions better. This service, along with Prometheus and Grafana, will run inside multiple Docker components using docker-compose to deploy

## Techniques employed

- Software architecture and design
- A mix of data science and data engineering
- **Microservices**: FastAPI
- **Anomaly detection**: Isolation forest model, scikit-learn and Plotly
- **Data analysis and visualization**: seaborn
- **Monitoring and metrics**: Prometheus, prometheus_client, and Grafana
- **Dockerizing**: Docker, Docker-Compose

## To run locally

- `docker compose up`
- Navigate to localhost:4001
  - password = password
