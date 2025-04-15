FROM apify/actor-python

COPY . ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "main.py"]
