# Base image
FRO# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Add shell script to run migrations and start gunicorn
COPY run.sh .
RUN chmod +x run.sh

# Environment configs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Start the app using the shell script
CMD ["./run.sh"]
