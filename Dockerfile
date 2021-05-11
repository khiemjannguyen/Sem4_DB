FROM python:3.8.5-slim

# update pip
RUN pip install --upgrade pip

# add new user
RUN useradd -ms /bin/bash khiem

# use new user
USER khiem

# go to workdir
WORKDIR /home/khiem/app

COPY --chown=khiem scraper/requirements.txt /home/khiem/app

RUN pip install -r requirements.txt

COPY --chown=khiem scraper/ /home/khiem/app

CMD ["python3", "main.py"]