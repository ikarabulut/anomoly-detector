FROM python:3.7

WORKDIR /src
ENV JUPYTER_TOKEN="password"

RUN pip install jupyter

COPY . /src

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=4001", "--no-browser", "--allow-root"]