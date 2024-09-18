#!/bin/bash

git checkout master
git pull origin master

/usr/local/bin/docker-compose down
/usr/local/bin/docker-compose up -build

echo "Deployment completed successfully"
