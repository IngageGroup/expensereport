FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY ./backend /app
WORKDIR /app
RUN chmod +x ./bash/logo.sh
RUN ./bash/logo.sh
ENV EXPENSE_REPORT_APP_SETTINGS=/app/config/DOCKERCONFIG.py
RUN mkdir -p uploads
RUN pip install -r requirements.txt
