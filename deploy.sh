#!/bin/bash

export PATH=$PATH:/usr/local/bin

git checkout master
git pull origin master

docker-compose down
docker-compose up -build

echo "Deployment completed successfully"
