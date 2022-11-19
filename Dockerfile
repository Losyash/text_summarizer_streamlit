FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "streamlitapp", "/bin/bash", "-c"]

COPY ./src .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "streamlitapp", "streamlit", "run", "app.py"]