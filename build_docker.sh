#!/bin/sh
AUTHOR=`cat author.txt`
NAME=`cat name.txt`
VERSION=`cat version.txt`

docker image build . -t "$AUTHOR/$NAME:$VERSION" --build-arg AUTHOR=$AUTHOR --build-arg NAME=$NAME --build-arg VERSION=$VERSION && \
  docker tag "$AUTHOR/$NAME:$VERSION" "$AUTHOR/$NAME:latest"
