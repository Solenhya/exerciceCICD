# Use Python 3.12 as the base image Selection <3.13 pour compatibalité et >=3.12 pour le formatage améliorer
FROM python:3.12-slim

# Set working directory
WORKDIR /app


# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .
# Command to run the application
CMD ["python", "programme.py"]
