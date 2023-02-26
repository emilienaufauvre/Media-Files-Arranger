import datetime
import logging
import os
import pathlib
import shutil
import sys

import filetype
import pytz

from src.date import DATE_MAX, Date
from src.parse_date import parse_date

_FILE_FORMAT = "%Y:%m:%d_%H:%M:%S:%f"
_TIME_ZONE = "Europe/Paris"
_ERROR_MSG = "%s\n" \
             "\tUsage: main.py PATH1 PATH2\n" \
             "\tPATH1: root directory of a tree to be parsed\n" \
             "\tPATH2: output directory to store parsed files"


def check_usage_and_get_args() -> (str, str):
    """
    Check the correct usage from CLI, and extract the arguments.

    :rtype: (str, str).
    :return: A path to the root directory of a tree structure to be parsed,
        and a path to an existing directory that will be used to store the
        parsed files.
    """
    if len(sys.argv) != 3:
        logging.error(_ERROR_MSG % "Incorrect number of arguments.")
        exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not input_path:
        logging.error(_ERROR_MSG % "a PATH1 is empty.")
        exit(1)
    if not output_path:
        logging.error(_ERROR_MSG % "a PATH2 is empty.")
        exit(1)
    if not os.path.exists(input_path):
        logging.error(_ERROR_MSG % "PATH1 does not exist.")
        exit(1)
    if not os.path.exists(output_path):
        logging.error(_ERROR_MSG % "PATH2 does not exist.")
        exit(1)
    if not os.path.isdir(input_path):
        logging.error(_ERROR_MSG % "PATH1 is not a directory.")
        exit(1)
    if not os.path.isdir(output_path):
        logging.error(_ERROR_MSG % "PATH2 is not a directory.")
        exit(1)

    return input_path, output_path


def set_logger() -> None:
    """
    Set up the default logger to catch every message, and to write them on
    stdout.

    :rtype: NoneType.
    :return: None.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(funcName)s::%(lineno)d:\t%(message)s",
        stream=sys.stdout,
    )


def parse_pictures_and_videos(dir_to_be_parsed: str,
                              dir_to_store_parsed_files: str) -> None:
    """
    Parse the given tree, find media files, rename them, and store them in the
    given directory.

    :param str dir_to_be_parsed: A path to the root directory of a tree
        structure to be parsed,
    :param str dir_to_store_parsed_files: A path to an existing directory that
        will be used to store the parsed files.
    :rtype: NoneType.
    :return: None.
    """
    # Parse all the directories in the given tree.
    for root, dirs, files in os.walk(dir_to_be_parsed):
        logging.debug("> Parsing %s" % root)
        # Parse all the file in the current directory.
        for file in files:
            # Get the full file path and its extension.
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)
            # Check if the file is a media.
            if filetype.is_image(file_path) or filetype.is_video(file_path):
                # Get the creation time of the file.
                file_time_of_creation = extract_creation_time(file_path,
                                                              file_name)
                # Define the path to the output dir using the new name.
                file_path_new_name = "%s%s" % (
                    os.path.join(dir_to_store_parsed_files,
                                 str(file_time_of_creation)),
                    file_extension,
                )
                # Copy the file to the new path.
                shutil.copy(file_path, file_path_new_name)
                logging.debug(
                    "\tOK: %s - renamed to %s." % (
                        file_path, file_time_of_creation)
                )
            else:
                logging.debug("\tKO: %s - not a media." % file_path)


def get_creation_time(path: str) -> Date:
    """
    Get the creation time of a file using file system.

    :param str path: A path to an existing file.
    :return: A date.
    """
    f = pathlib.Path(path)
    t = f.stat().st_ctime
    t = datetime.datetime.fromtimestamp(
        t,
        tz=pytz.timezone(_TIME_ZONE),
    )
    return Date.create_from_datetime(t)


def extract_creation_time(path: str, name: str) -> Date:
    # Get file system creation time.
    creation_time_fs = get_creation_time(path)
    # Get file name creation time.
    print(name)
    creation_time_fn = parse_date(name)
    if not creation_time_fn:
        creation_time_fn = DATE_MAX
    # Return the lowest date.
    return min(creation_time_fs, creation_time_fn)


def main():
    s = "WP_2023_12_12_12_12"
    input_dir, output_dir = check_usage_and_get_args()
    set_logger()
    parse_pictures_and_videos(input_dir, output_dir)


if __name__ == "__main__":
    main()
