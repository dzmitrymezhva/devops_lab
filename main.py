import argparse
import tempfile
import zipfile
import logging
import shutil
import sys
import os


logging.basicConfig(
    filename='homework7.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


def check_all_folders(path_to_folder):
    indicate = False
    folders = []
    for f in os.scandir(path_to_folder):
        if f.is_dir():
            folders.append(f.path)
        if f.is_file() and f.name == "__init__.py":
            indicate = True
    if indicate:
        for item in folders:
            check_all_folders(item)
    else:
        shutil.rmtree(path_to_folder)
        logging.info("Folder " + path_to_folder + " deleted.")


def get_zip_archive(path_to_folder, old_name_archive):
    with zipfile.ZipFile(old_name_archive[:-4] + "_new.zip", "w") as zip_file:
        for dirpath, dirnames, files in os.walk(path_to_folder):
            for file in files:
                filenames = os.path.join(dirpath, file)
                archivenames = filenames[(len(path_to_folder)):]
                zip_file.write(filenames, archivenames)
    logging.info("New archive " + old_name_archive[:-4] + "_new.zip created.")


parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Zip file name")
args = parser.parse_args()
logging.debug("Archive name: " + args.n)

with tempfile.TemporaryDirectory() as temp_folder:
    logging.info("Temporary folder created.")
    try:
        with zipfile.ZipFile(args.n, 'r') as zip_ref:
            zip_ref.extractall(temp_folder)
            logging.info("Archive extracted.")

    except OSError as error:
        logging.error(error)
        sys.exit()

    check_all_folders(temp_folder)
    logging.info("Everything checked.")
    get_zip_archive(temp_folder, args.n)
