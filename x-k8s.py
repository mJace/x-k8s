#!/usr/bin/env python3

""" X-K8S Installer

Usage: 
    ./x-k8s.py install
    ./x-k8s.py ( -h | --help)
    ./x-k8s.py ( -v | --version)

Examples:
    ./x-k8s.py install
    ./x-k8s.py -h
    ./x-k8s.py --help
    ./x-k8s.py -v
    ./x-k8s.py --version

Options:
    -h, --help
    -v, --version

"""

from docopt import docopt
from pathlib import Path

basePath = Path().absolute()
inventoryPath = basePath+'/kubespray/inventory/mycluster/hosts.ini'
playbookPath = basePath+'/kubespray/cluster.yml'

def install():
    mycli = getattr(__import__("ansible.cli.playbook", fromlist=['PlaybookCLI']), 'PlaybookCLI')
    args = ['ansible-playbook', '-i', inventoryPath, playbookPath]
    cli = mycli(arg)
    cli.parse()
    exitCode = cli.run()
    print(exitCode) 

def main():
    global arg
    print(arg)

if __name__ == "__main__":
    arg = docopt(__doc__, version='v1.0.1')
    main()