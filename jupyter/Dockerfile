FROM python:3.11

WORKDIR /src

ENV JUPYTER_TOKEN="password"
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VERSION=1.3.1

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-interaction

COPY . ./

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]