import os, subprocess, logging, json

from pathlib import Path
from sys import exc_info
from pprint import pprint

CONFIG_FILE = "config.json"

def main():
    os.chdir(Path().absolute())

    with open(CONFIG_FILE) as config:
        data = json.load(config)
        pprint(data)

        build_paths = data["build_paths"]
        engine_path = data["engine_path"]
        export_path = data ["export_path"]
        command_line_format = data["command_line_format"]

        for child_path in build_paths:
            path = Path(child_path)
            if path.exists() and path.is_dir():
                build_unity_from_path(path, engine_path, export_path, command_line_format)


    input("Build Process Ended")
    return

def build_unity_from_path(path, engine_path, export_path, command_line_format):
    try:
        command_line = command_line_format.format( engine_path, path, export_path)
        print("Exec:" + command_line)
        args = command_line.split(' ')
        subprocess.run(args, capture_output=True)
    except:
        print("Unexpected error: ", exc_info())


main()
