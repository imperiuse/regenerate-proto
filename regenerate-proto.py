#!/usr/bin/env python

import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Compile protobufs to python pb')
    parser.add_argument('--proto_dir', type=str, help='directory with proto files', default=os.curdir)
    parser.add_argument('--out_dir', type=str, help='output dir for generated code', default=".")
    parser.add_argument('--python', dest='python', action='store_true')
    parser.add_argument('--golang', dest='golang', action='store_true')
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


def get_proto(root: str) -> []:
    proto_dirs = []
    for dirpath, _, fnames in os.walk(root):
        for fname in fnames:
            if fname.endswith(".proto"):
               proto_dirs.append(dirpath)
               break  # need only dir name

    return proto_dirs


if __name__ == "__main__":
    args = parse_args()
    print(f"Dir for search .proto files: {args.proto_dir}")
    print(f"Output dir: {args.out_dir}")
    print(f"Generate code for Python: {args.python}")
    print(f"Generate code for Golang: {args.golang}")

    proto_dirs = get_proto(args.proto_dir)
    print(f"Found proto dirs: {proto_dirs}")

    for dir in proto_dirs:
        if args.python:
            proto_build_cmd = PYTHON_PROTOC_TEMPLATE.format(
                I="/".join(dir.split('/')[:-2]),
                python_out=args.out_dir,
                grpc_python_out=args.out_dir,
                proto=os.path.join(dir, "*.proto"))
            print(f"[Python]: {proto_build_cmd}")
            os.system(proto_build_cmd)
        elif args.golang:
            proto_build_cmd = GOLANG_PROTOC_TEMPLATE.format(
                I="/".join(dir.split('/')[:-2]),
                go_out=args.out_dir,
                proto=os.path.join(dir, "*.proto"))
            print(f"[Golang]: {proto_build_cmd}")
            os.system(proto_build_cmd)





