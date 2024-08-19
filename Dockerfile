FROM python:3.12.1

WORKDIR /app

RUN pip install streamlit

EXPOSE 8501

COPY . /app

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
