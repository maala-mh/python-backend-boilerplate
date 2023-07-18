FROM python:3.11

WORKDIR /src
EXPOSE 8080

# ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6

RUN apt-get update && \
    apt-get install -y curl perl-modules procps vim-tiny && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*


RUN pip install poetry==1.5.1
RUN poetry config virtualenvs.create false
COPY poetry.lock /src/
COPY pyproject.toml /src/
RUN poetry install

COPY . /src

RUN chmod +x /src/bin/run.sh

# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

CMD ["/src/bin/run.sh"]
