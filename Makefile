 IMAGE_NAME = python-logging-example

run: build
	docker run --rm -it $(IMAGE_NAME)

build: Dockerfile main.py
	docker build -t $(IMAGE_NAME) .

.PHONY: run build
.DEFAULT: run