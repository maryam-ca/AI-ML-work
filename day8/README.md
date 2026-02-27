# Week 2 - Day 8 Docker

## Build Image
docker build -t week2-api:day8 .

## Run Container
docker run --rm -p 8000:8000 --env-file docker.env week2-api:day8

## Test
http://127.0.0.1:8000/docs
