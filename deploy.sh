#!/bin/bash

docker compose down
docker compose build
docker compose up
echo "Deployment completed successfully"