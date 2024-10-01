# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure pip is updated
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install -r requirements.txt

# If using gRPC, also install gRPC tools if needed
# RUN pip install grpcio grpcio-tools

# Expose the port on which your gRPC server runs (adjust based on your server's config)
EXPOSE 50051

# Define environment variables, if any
ENV PYTHONUNBUFFERED=1

# Run the Python application
CMD ["python3", "main_server.py"]
