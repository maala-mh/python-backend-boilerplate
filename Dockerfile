FROM python:3.11-slim

WORKDIR /src
EXPOSE 8080

RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    libxrender1 \
    libfontconfig1 \
    && apt-get clean

RUN pip install poetry==1.5.1
RUN poetry config virtualenvs.create false
COPY poetry.lock /src/
COPY pyproject.toml /src/
RUN poetry install

COPY . /src
RUN cd /src && python setup.py develop

RUN chmod +x /src/bin/run.sh

# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

CMD ["/src/bin/run.sh"]
