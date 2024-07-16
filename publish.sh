#!/bin/sh
AUTHOR=`cat author.txt`
NAME=`cat name.txt`
VERSION=`cat version.txt`

./build_docker_prod.sh && \
  docker tag "$AUTHOR/$NAME:$VERSION" "$AUTHOR/$NAME:latest" && \
  docker push "$AUTHOR/$NAME:$VERSION" && \
  docker push "$AUTHOR/$NAME:latest" && \
  docker rmi "$AUTHOR/$NAME:latest" && \
  docker rmi "$AUTHOR/$NAME:$VERSION"
