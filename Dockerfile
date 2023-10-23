FROM python:latest

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD [ "uvicorn", "src.main:app" ]

