import fnmatch
import os
import py_compile
import string
from pathlib import Path
from zipfile import PyZipFile, ZIP_STORED

from utils.utils import prepare_directory


def compile_py(src: string, dest: string):
    # Compile the mod
    for root, dirs, files in os.walk(src):
        for filename in fnmatch.filter(files, '*.py'):
            src_py = root + '/' + filename
            relative_path = str(Path(root).relative_to(src))
            desc_path = dest + '/' + relative_path
            compile_pyc = desc_path + '/' + filename.replace('.py', '.pyc')

            print(f"Source: {src_py} compile: {desc_path + '/' + filename.replace('.py', '.pyc')}")
            py_compile.compile(src_py, compile_pyc)

def start_compile():
    prepare_directory('build/sentient_sims')

    compile_py('sentient_sims', 'build/sentient_sims')


start_compile()
