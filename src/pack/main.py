from os import walk
from os.path import join, relpath
from pathlib import Path
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
    project_root = Path(__file__).parent.parent.parent
    dest = project_root.joinpath("app.zip")
    src = project_root.joinpath("src", "compound")
    requirements = project_root.joinpath("requirements.txt")

    compress_folder(src, dest, requirements)
