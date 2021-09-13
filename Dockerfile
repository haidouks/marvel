FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements_prod.txt
CMD [ "python3", "cli.py" ]