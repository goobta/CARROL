#!/bin/sh

docker run --rm \
					 --name CARROL-cpu \
					 -p 8889:8888 \
					 -v $(pwd)/../src:/root/workspace \
					 cs534:cpu
