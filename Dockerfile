FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./app.py" ]