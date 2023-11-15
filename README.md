# Python logging template

Use the `logging` package and the `structlog` package to show basic and less basic logging configurations.

## FAQ
### Why do we need `PYTHONUNBUFFERED`?
Python will buffer `stdout` and `stderr` by default. In certain cases such as Python applications running in Docker containers, this will cause the output to not be immediately available.