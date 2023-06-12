FROM python:3.9

RUN mkdir -p /ci_cd_test
WORKDIR /ci_cd_test
ADD . /ci_cd_test

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app"]