import tarfile

def open_tarfile_function(tarfile_file_name):
    open_tarfile=tarfile.open("python-stdnum-1.8.tar_.gz")
    open_tarfile.extractall(path='stdnum')
    open_tarfile.close()

open_tarfile_function('data.tgz')