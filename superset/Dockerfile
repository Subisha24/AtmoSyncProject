FROM apache/superset:latest

USER root

RUN . /app/.venv/bin/activate && \
    uv pip install snowflake-sqlalchemy

USER superset