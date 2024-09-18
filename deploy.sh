#!/bin/bash

chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

git pull

docker-compose down
docker-compose up -build

echo "Deployment completed successfully"