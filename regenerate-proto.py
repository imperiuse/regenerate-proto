#!/usr/bin/env python

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Compile protobufs to python pb')
    parser.add_argument('--proto_dir', type=str, help='directory with proto files', default=os.curdir)
    parser.add_argument('--python', type=bool, help='generate python code', default=False)
    parser.add_argument('--golang', type=bool, help='generate golang code', default=False)
    return parser.parse_args()


PYTHON_PROTOC_TEMPLATE = "python3 -m grpc_tools.protoc " \
                         "-I {I} " \
                         "--python_out={python_out} " \
                         "--grpc_python_out={grpc_python_out} " \
                         "{proto}"

GOLANG_PROTOC_TEMPLATE = "protoc " \
                         "-I {I} " \
                         "--go_out=plugins=grpc:{go_out} " \
                         "{proto}"


def get_proto(root: str):
    protos = {}
    for dirpath, _, fnames in os.walk(root):
        for fname in fnames:
            if fname.endswith(".proto"):
               protos[fname] = dirpath

    return protos


if __name__ == "__main__":
    args = parse_args()
    print(f"Dir for search .proto files: {args.proto_dir}")
    print(f"Generate ccode for Python: {args.python}")
    print(f"Generate ccode for Golang: {args.golang}")

    proto_files = get_proto(args.proto_dir)
    print(f"Found proto files: {proto_files}")

    for proto_file, dir in proto_files.items():
        if args.python:
            proto_build_cmd = PYTHON_PROTOC_TEMPLATE.format(
                I="/".join(dir.split('/')[:-2]),
                python_out=".",
                grpc_python_out=".",
                proto=os.path.join(dir, proto_file))
            print(f"[Python]: {proto_build_cmd}")
            os.system(proto_build_cmd)
        elif args.golang:
            proto_build_cmd = GOLANG_PROTOC_TEMPLATE.format(
                I="/".join(dir.split('/')[:-2]),
                golang_out=".",
                proto=os.path.join(dir, proto_file))
            print(f"[Golang]: {proto_build_cmd}")
            os.system(proto_build_cmd)





