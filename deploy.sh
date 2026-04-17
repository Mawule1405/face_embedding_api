#!/bin/bash

# Stop script on error
set -e

echo " Starting deployment..."

# Variables
IMAGE_NAME="insightface-api"
CONTAINER_NAME="insightface-container"
PORT=8000

#  Stop and remove existing container if exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo " Stopping existing container..."
    docker stop $CONTAINER_NAME || true
    docker rm $CONTAINER_NAME || true
fi

#  Optional: remove old image
if [ "$(docker images -q $IMAGE_NAME)" ]; then
    echo " Removing old image..."
    docker rmi $IMAGE_NAME || true
fi

#  Build image
echo " Building Docker image..."
docker build -t $IMAGE_NAME .

#  Run container
echo " Running container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $PORT:8000 \
    $IMAGE_NAME

#  Check container status
echo " Checking container..."
docker ps | grep $CONTAINER_NAME

echo " Deployment finished!"
echo " API available at: http://localhost:$PORT"