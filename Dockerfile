# Use a lightweight official Python image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 80 to the outside world
EXPOSE 80

# Run the application
CMD ["python", "app.py"]