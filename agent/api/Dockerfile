FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
cp /root/.local/bin/uv /usr/local/bin/

ENV PATH="/root/.cargo/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock* ./
COPY . .

RUN uv venv

RUN ls -la 

RUN uv pip install -r pyproject.toml

EXPOSE 8000

CMD ["uv", "run", "/app/src/__main__.py"]