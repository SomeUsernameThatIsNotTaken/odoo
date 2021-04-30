import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.sep)

output_filename = "python-stdnum-1.8.tar.gz"
source_dir = "stdnum\python-stdnum-1.8"

make_tarfile(output_filename, source_dir)