#!/usr/bin/env bash

echo "Generate Python *.pb"
python3 ./regenerate-proto.py --proto_dir ./api --python

echo "Generate Golang *.pb"
python3 ./regenerate-proto.py --proto_dir ./api --golang