FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 
COPY python_server/ /server/
WORKDIR /server
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 
CMD python3 main.py

