#!/bin/bash

git checkout master
git pull

chmod +x /usr/local/bin/docker-compose
docker-compose --version

docker-compose down
docker-compose up -build

echo "Deployment completed successfully"