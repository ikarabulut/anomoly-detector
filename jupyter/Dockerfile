FROM python:3.7

WORKDIR /src
ENV JUPYTER_TOKEN="password"

COPY . /src

RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]