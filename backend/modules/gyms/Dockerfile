# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port (change if needed)
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]