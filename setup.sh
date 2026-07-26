#!/bin/bash

echo "==================================="
echo " Robot Head Setup"
echo "==================================="

sudo apt update

sudo apt install -y \
python3-opencv \
python3-picamera2 \
python3-pip \
git

pip3 install -r requirements.txt

mkdir -p models

wget -O models/haarcascade_frontalface_default.xml \
https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

echo ""
echo "==================================="
echo "Setup Completed Successfully!"
echo "Run:"
echo "python3 src/main.py"
echo "==================================="
