FROM apify/actor-python-playwright:latest

# Copy only requirements first to leverage layer caching (locally or if reused)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the project
COPY . ./

# Run the main script
CMD ["python", "main.py"]
