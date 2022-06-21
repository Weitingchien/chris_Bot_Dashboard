FROM python:3.9.13-buster
WORKDIR /app
ADD . /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
CMD ["python", "chrisdashboard.py"]