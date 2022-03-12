# -*- coding: utf-8 -*-

import os
import shutil
import zipfile

from pathlib import Path

import version as v


def create_missing_dir(p: Path) -> None:
    if not p.exists():
        p.mkdir(parents=True)


def is_libreoffice_available() -> bool:
    """ do we have regmerge somewhere (we suppose it is made available in current path var.) ? """
    return shutil.which("regmerge") is not None


def is_libreoffice_sdk_available() -> bool:
    """ do we have idlc somewhere (we suppose it is made available in current path var.) ? """
    return shutil.which("idlc") is not None


if __name__ == "__main__":
    plugin_version = v.__version__
    LO = "LibreOffice"
    XD = "XDontPanic"

    print(f'{LO} addin version: {plugin_version}')
    if is_libreoffice_available():
        print(f'{LO} binaries are in the path')
    else:
        print(f'no way to call {LO} binaries')
    if is_libreoffice_sdk_available():
        print(f'{LO} sdk binaries are in the path')
    else:
        print(f'no way to call {LO} sdk binaries')

    if is_libreoffice_available() and is_libreoffice_sdk_available():
        print('Compiling IDL source file')
        # remove previous files if any
        for p in [f'{XD}.rdb', f'{XD}.urd', f'dontpanic/{XD}.rdb']:
            if os.path.isfile(p):
                os.remove(p)
        os.system(f'idlc -w -C -cid {XD}.idl')
        os.system(f'regmerge {XD}.rdb /UCR {XD}.urd')
        # copy to addin directory
        shutil.copy(f'{XD}.rdb',f'dontpanic/{XD}.rdb')
    else:
        print('RDB file from version control will be used')

    EXTENSION_NAME = 'dontpanic'
    EXTENSION_SOURCE_DIRS = 'dontpanic'
    EXCLUDE_DIR = "pycache"

    outdir = Path("../out/")
    create_missing_dir(outdir)
    extension_archive = zipfile.ZipFile(outdir / f"{EXTENSION_NAME}.oxt", 'w')

    for dir_path, dirnames, filenames in os.walk(EXTENSION_SOURCE_DIRS):
        if EXCLUDE_DIR in dir_path:
            continue
        for name in filenames:
            file_path = dir_path + '/' + name
            print(file_path)
            if name == 'description.xml':
                description_content = open(file_path).read().replace('%PLUGIN_VERSION%', plugin_version)
                extension_archive.writestr(name, description_content)
            else:
                extension_archive.write(file_path, os.path.relpath(file_path, EXTENSION_SOURCE_DIRS))

    extension_archive.close()
    print('Successfully built LibreOffice addin version %s' % plugin_version)
