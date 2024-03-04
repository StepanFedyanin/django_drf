FROM python:3.12.2

#создает папку app#
RUN mkdir -p /app
#назначает папку app главной
WORKDIR /app

#обновляет зависимости
#RUN apt-get -y update



#копирует requirements в app
COPY requirements.txt ./requirements.txt
#устанавливает pip в app
RUN python -m pip install --upgrade pip
#скачивает зависимости
RUN pip install -r requirements.txt