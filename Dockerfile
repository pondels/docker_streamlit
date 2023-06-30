
# Pulls a working version of python to be used in our application
FROM python:3.8-slim

# Our working directory
WORKDIR /app

# Adds in the required documents for our application
COPY requirements.txt .

# Idk lmao
RUN pip install --no-cache-dir -r requirements.txt

# idk lmao
COPY app.py .

# Opens up the application under a port
EXPOSE 8501

# Runs the following line in the terminal
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]