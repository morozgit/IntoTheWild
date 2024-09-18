#!/bin/bash

git checkout master
git pull

docker-compose down
docker-compose up -build

echo "Deployment completed successfully"