#!/bin/sh

docker run --runtime=nvidia -it --rm --name CARROL-gpu -p 8889:8888 cs534:gpu
