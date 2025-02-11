FROM python:3.10.6

WORKDIR /app

ENV NEO4J_URI=bolt://a9b3d3bd6a2cd4b56b1b94e1b77842f0-1055723587.us-east-1.elb.amazonaws.com:7687
ENV USER_NAME=neo4j
ENV PASSWORD=1234

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
