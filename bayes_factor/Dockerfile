FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install scipy --break-system-packages

WORKDIR /workspace

COPY bayes_factor ./bayes_factor

CMD ["python3", "-m", "unittest", "discover", "-s", "bayes_factor/tests", "-v"]
