## Build proto files python tool

Available lang:

* Python
* Golang

### Before

Install grpc support software (`install.sh`):

    # For Golang
    go get -u google.golang.org/grpc
    go get -u github.com/golang/protobuf/protoc-gen-go
    export PATH=$PATH:$GOPATH/bin
    
    #For Python
    python3 -m pip install --upgrade pip
    python3 -m pip install grpcio
    python3 -m pip install grpcio-tools

For more information see here -> https://grpc.io/docs/quickstart/


### Usage:
    
    echo "Generate Python *.pb"
    python3 ./regenerate-proto.py --proto_dir ./api --python

    echo "Generate Golang *.pb"
    python3 ./regenerate-proto.py --proto_dir ./api --golang



### More here -> https://medium.com/red-crane/grpc-and-why-it-can-save-you-development-time-436168fd0cbc