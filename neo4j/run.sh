#!/bin/bash

docker container prune --force
docker-compose up --build
