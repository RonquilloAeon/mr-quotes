FROM python:3.8.0-slim as python

# Base
FROM python as base
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src ./src/
COPY MANIFEST.in setup.py ./

EXPOSE 8000

# Dev
FROM base as develop
COPY --from=base / /

COPY start.dev.sh setup.py ./

RUN pip3 install --no-cache-dir -e . watchdog==0.9.0

# Pre-Prod
FROM base as pre-production
COPY --from=base / /

RUN pip3 install --no-cache-dir --no-warn-script-location --user .

# Prod
FROM python as production
COPY --from=pre-production /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY start.sh ./

ENTRYPOINT ["/app/start.sh"]
