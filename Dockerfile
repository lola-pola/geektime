FROM python:3.9

WORKDIR /app
COPY app .
COPY req req
RUN pip install -r req

<<<<<<< HEAD
CMD ["streamlit", "run" , "app.py","--server.port","80"]
=======
CMD ["streamlit", "run" , "bot.py","--server.port","80"]
>>>>>>> bbe5b1d (adding)
