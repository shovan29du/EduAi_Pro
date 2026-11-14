FROM python:3.11-slim

WORKDIR /app

# Toolchains for the Code Editor's /api/run-code endpoint (one compiler/
# interpreter per supported language). This is a heavyweight layer (JDK, Go,
# Rust, Mono, etc. easily add 1GB+) -- if image size/build time becomes a
# problem on a constrained hosting tier, trim languages here and in
# app/main.py's run_code()/CodeEditor.jsx's LANGUAGES list together.
RUN apt-get update && apt-get install -y --no-install-recommends \
        g++ \
        gfortran \
        gcc \
        default-jdk-headless \
        mono-devel \
        golang-go \
        rustc \
        php-cli \
        ruby \
        perl \
        r-base-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
