# -*- coding: utf-8 -*-

from pathlib import Path
import build as b


if __name__ == "__main__":
    print(f'{b.LO} addin version: {b.plugin_version}')

    with open(Path(f"./{b.EXTENSION_NAME}.update.xml")) as infile:
        with open(Path(f"../{b.EXTENSION_NAME}.update.xml"), 'w') as of:
            of.write(infile.read().replace('%PLUGIN_VERSION%', b.plugin_version))

    print(f'Successfully built {b.LO} update.xml version {b.plugin_version}')
