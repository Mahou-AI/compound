from os import walk, environ
from os.path import join, relpath
from pathlib import Path
from sys import argv
from zipfile import ZipFile


def compress_folder(
    src: str,
    dest: str,
    requirements: str,
):
    with ZipFile(dest, "w") as output:
        output.write(requirements, "requirements.txt")

        for root, _, files in walk(src):
            for file in files:
                path = join(root, file)
                output.write(path, relpath(path, src))


if __name__ == "__main__":
    dest: str
    if "OUTPUT_PATH" in environ:
        dest = environ["OUTPUT_PATH"]
    elif "-o" in argv:
        dest = argv[argv.index("-o") + 1]
    else:
        dest = input("output: ")

    src = Path(__file__).parent.parent.joinpath("compound")
    requirements = Path(__file__).parent.parent.parent.joinpath("requirements.txt")

    compress_folder(src, dest, requirements)
