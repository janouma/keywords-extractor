#!/bin/sh
AUTHOR=`cat author.txt`
NAME=`cat name.txt`
VERSION=`cat version.txt`

docker push "$AUTHOR/$NAME:$VERSION" && \
  docker push "$AUTHOR/$NAME:latest" && \
  docker rmi -f $(docker images --filter "label=com.heimdallinsight-fully-qualified-name=$AUTHOR/$NAME:$VERSION" -q)
