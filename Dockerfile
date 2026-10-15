FROM python:3.12-slim
WORKDIR /work
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY experiments/ ./experiments/
COPY run_all.sh .
CMD ["bash", "run_all.sh"]
