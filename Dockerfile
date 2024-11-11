# Stage 1: Build Stage
FROM python:3.11-alpine AS builder

# Set environment variables to avoid Python writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install necessary build dependencies
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev postgresql-dev

# Create a directory for the application
WORKDIR /users

# Copy the requirements file to install dependencies
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime Stage
FROM python:3.11-alpine

# Adds metadata to the current image
LABEL author="srikanth"

# Set environment variables to avoid Python writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgresql://srikanth:srikanthkovuri@localhost:5432/library

# Install runtime dependencies, including PostgreSQL client libraries
RUN apk add --no-cache libpq bash

# Create a directory for the application
WORKDIR /app

# Create a new user and group for enhanced security
RUN addgroup -S appgroup && adduser -S -G appgroup -h /home/srikanth -D srikanth

# Set the correct permissions for the application directories
RUN mkdir -p /app /data /logs && \
    chown -R srikanth:appgroup /app /data /logs

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application source code to the working directory
COPY . .

# Change ownership of the application files
RUN chown -R srikanth:appgroup /app

# Switch to the non-root user
USER srikanth

# Ensure uvicorn is installed in case it wasn't properly copied or was missed
RUN pip install --no-cache-dir uvicorn

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
