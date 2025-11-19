# Base Image
FROM python:3.12

# Set working directory inside container
WORKDIR /app

# Copy everything from current folder to /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
ENTRYPOINT ["python", "main.py"]
