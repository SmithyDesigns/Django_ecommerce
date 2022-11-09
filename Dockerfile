FROM pypy:latest
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3" , "ecommerce"]