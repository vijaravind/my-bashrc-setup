#!/usr/bin/env python


"""
Python script to do the following:
    + create relevant symbolic links for `.bashrc`, `.bash_aliases` files
      and `.bashrc.d` folder.
"""


import os, sys


def make_symbolic_links(dir_path):
    wk_dir = os.environ['HOME']
    bashrc_path = os.path.join(dir_path, 'bashrc')
    bash_aliases_path = os.path.join(dir_path, 'bash_aliases')
    bashrc_dir_path = os.path.join(dir_path, 'bashrc.d')
    ln_pattern = "ln -s {0} {1}"
    os.chdir(wk_dir)
    os.system(ln_pattern.format(bashrc_path, '.bashrc'))
    os.system(ln_pattern.format(bash_aliases_path, '.bash_aliases'))
    os.system(ln_pattern.format(bashrc_dir_path, '.bashrc.d'))


def main():
    curr_file_path = os.path.realpath(__file__)
    curr_dir_path = os.path.dirname(curr_file_path)
    os.chdir(curr_dir_path)
    make_symbolic_links(curr_dir_path)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("shutting down...")
        sys.exit(0)


