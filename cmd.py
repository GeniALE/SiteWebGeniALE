#!/usr/bin/python3

import os
import click

"""
Python script will some command shortcut. 
"""

@click.group()
def cli():
    pass


@cli.command()
def dockerUp():
    os.system('docker-compose -f ./docker/dc.db.yml up -d')
    click.echo('Started docker')


@cli.command()
def dockerDown():
    os.system('docker-compose -f ./docker/dc.db.yml down')
    click.echo('Stopped docker')


if __name__ == '__main__':
    cli()
