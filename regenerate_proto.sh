#!/usr/bin/env bash

rm -rf ./internal/grpc
mkdir -p ./internal/grpc
echo "Generate Golang *.pb"
python3 ./tools/regenerate-proto/regenerate-proto.py --proto_dir ./api --out_dir ./internal/grpc --golang

rm -rf ./grpc
mkdir -p ./grpc
echo "Generate Python *.pb"
python3 ./tools/regenerate-proto/regenerate-proto.py --proto_dir ./api --out_dir ./grpc --python
sed -i -E 's/^from /from grpc./g' ./grpc/*/proto/*_grpc.py