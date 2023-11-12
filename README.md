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

**Jupyter Notebook**: To run the jupyter notebook and view the notebooks from the repository run:

1. `docker compose up jupyter`
2. Navigate to `http://localhost:8888/?token=password`
   You can also use the jupyter server within your vscode as well by connecting to the same url while the container is running.

**API**: To run the API with the most recent model run:

1. `docker compose up api`
2. Navigate to `http://localhost:8000/model_information` this will return the info of the deployed model.

## To update the model

Run the jupyter notebook locally and navigate to `train.ipynb` if you want to update the csv's you can as well. Or you can update the `IsolationForest()` parameters.

If you run `dump(clf, 'model.joblib')` at the end of the notebook you will have a new `model.joblib` exported within your `/jupyter` directory. Move that file to the `/service` directory. When you rebuild and run the `api` Dockerfile it will use the new model.

## API Docs

To view the swagger docs navigate to `http://localhost:8000/docs`

`/model_information`

`GET`: This will return the information of the deployed model.

`/prediction`

`POST`: Accepts as input an object with a field named `feature_vector` of type `List[float]`. This field takes the vector we will input to the model to predict. The input object needs a second, but optional, field named `score` of type bool. If `score` is set to `true` then the response will include `anomoly_score`
Request body schema:

```
{
  "feature_vector": [
    0
  ],
  "score": false
}
```
