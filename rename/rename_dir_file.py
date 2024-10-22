import pathlib
import sys

def rename(path: pathlib.Path):
    if not path.exists():
        return
    if not path.is_dir():
        return

    for item in path.rglob("*"):
        if " " in item.name:
            new_name = item.name.replace(" ", "_")
            new_path = item.parent / new_name
            item.rename(new_path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = pathlib.Path(sys.argv[1])
    rename(path)