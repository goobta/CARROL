#!/bin/sh

docker run \
	--runtime=nvidia \
	--rm \
 	--name CARROL-gpu \
 	-p 8889:8888 \
	-v $(pwd)/../src:/root/workspace \
 	cs534:gpu
