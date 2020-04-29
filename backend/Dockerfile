FROM python:alpine3.7 
COPY ./backend /app
WORKDIR /app
ENV EXPENSE_REPORT_APP_SETTINGS=/app/config/DOCKERCONFIG.py
RUN mkdir -p uploads
RUN pip install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "api.py" ] 
