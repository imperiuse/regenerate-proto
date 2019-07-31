#!/usr/bin/env bash

mkdir -p ./proto

echo "Generate Python *.pb"
python3 ./tools/regenerate-proto/regenerate-proto.py --proto_dir ./api --out_dir ./proto --python

echo "Generate Golang *.pb"
python3 ./tools/regenerate-proto/regenerate-proto.py --proto_dir ./api --out_dir ./proto --golang