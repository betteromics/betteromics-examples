FROM python:3.11-slim-buster

WORKDIR /root
ENV VENV /opt/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root

RUN apt-get update && apt-get install -y build-essential curl gnupg docker

RUN curl 'https://packages.adoptium.net/artifactory/api/gpg/key/public' | apt-key add - && \
    echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list &&\
    apt-get update &&\
    apt-get install -y temurin-17-jre

# need this version so that nextflow can read files from S3 without credential finding issues
ENV NXF_VER 23.06.0-edge

RUN curl -s https://get.nextflow.io | bash \
    && mv nextflow /usr/bin/

ENV VENV /opt/venv
# Virtual environment
RUN python3 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"

# Install Python dependencies
COPY requirements.txt /root
RUN pip install -r /root/requirements.txt

# Copy the actual code
COPY . /root

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
