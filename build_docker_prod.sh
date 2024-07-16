#!/bin/sh
AUTHOR=`cat author.txt`
NAME=`cat name.txt`
VERSION=`cat version.txt`
docker image build --platform linux/amd64 . -t "$AUTHOR/$NAME:$VERSION" --build-arg AUTHOR=$AUTHOR --build-arg NAME=$NAME --build-arg VERSION=$VERSION
