"""
Typer decorators.
"""

import typer
from .courier import Courier


Typer = typer.Typer()


@Typer.command()
def read_docs(file="help.txt"):
    Courier.read_docs(file)

@Typer.command()
def get_package_created():
    Courier().get_package_created()

@Typer.command()
def help(args, get_test=False):
    Courier.proc_args(args, get_test)
