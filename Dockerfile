FROM python:3.8

ADD ./ ./

RUN pip install -r requirements.txt

RUN pip install .

CMD python3 -m email_notion_database.main
