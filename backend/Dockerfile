FROM python:alpine3.7 
COPY ./backend /app
WORKDIR /app
RUN mkdir uploads
RUN pip install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "api.py" ] 
