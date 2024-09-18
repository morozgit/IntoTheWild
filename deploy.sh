#!/bin/bash

git checkout master
git pull

docker compose down
docker compose build
docker compose up

echo "Deployment completed successfully"