#!/usr/bin/env bash

# For Golang
go get -u google.golang.org/grpc
go get -u github.com/golang/protobuf/protoc-gen-go
export PATH=$PATH:$GOPATH/bin

#For Python
python3 -m pip install --upgrade pip
python3 -m pip install grpcio
python3 -m pip install grpcio-tools


