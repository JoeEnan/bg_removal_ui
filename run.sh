#!/bin/bash

if [ -f "docker-compose.traefik.yml" ]; then
    docker-compose -f docker-compose.yml -f docker-compose.traefik.yml up "$@"
else
    docker-compose -f docker-compose.yml up "$@"
fi