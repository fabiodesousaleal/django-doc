# Dockerfile
FROM ubuntu:22.04

ENV TZ America/Sao_Paulo
ENV NODE_VERSION=20.11.1

WORKDIR /app

COPY requirements.txt .

RUN apt update -y && apt install -y python3.11 python3.11-venv python3-pip curl && python3.11 -m venv /venv 

ENV PATH="/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt && \
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install ${NODE_VERSION}

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata

RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

RUN dpkg-reconfigure --frontend noninteractive tzdata

# DATABASE postgres - requeriments
#RUN pip install psycopg2-binary

EXPOSE 8000

CMD ["bash", "-c", "source /venv/bin/activate && python3 manage.py runserver 0.0.0.0:8000"]