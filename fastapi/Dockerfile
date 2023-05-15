FROM python:3.10

WORKDIR .

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]