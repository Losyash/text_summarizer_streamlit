FROM continuumio/miniconda3

WORKDIR /app

COPY environments.yml .
RUN conda env create -f environments.yml

SHELL ["conda", "run", "-n", "streamlitapp", "/bin/bash", "-c"]

COPY app.py .
COPY ./src ./src

EXPOSE 8051
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "streamlitapp", "streamlit", "run", "app.py"]