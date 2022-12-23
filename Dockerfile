FROM pypy:latest
WORKDIR /app
RUN python -m pip install -U pip setuptools wheel
RUN pip install spacy
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md
COPY . /app
CMD python semantic.py