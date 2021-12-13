FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE $PORT
RUN python manage.py collectstatic --noinput
CMD python3 manage.py runserver 0.0.0.0:$PORT