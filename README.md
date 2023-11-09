# Anomoly Detector

Currently this app has functionality to run a jupyter notebook in a docker container to view the hello-world notebook.

## Techniques employed

- Software architecture and design
- A mix of data science and data engineering
- Microservices: FastAPI
- Anomaly detection: Isolation forest model, scikit-learn and Plotly
- Data analysis and visualization: seaborn
- Monitoring and metrics: Prometheus, prometheus_client, and Grafana
- Dockerizing: Docker, Docker-Compose

## To run locally

- Navigate to `./anomoly_detector/jupyter`
- Run `docker build . -t notebook`
- Run `docker run -d -p 4001:4001 notebook`
