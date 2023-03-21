"""
Typer decorators.
"""

import typer
import courier


Typer = typer.Typer()


@Typer.command()
def read_docs():
    courier.Courier.read_docs()

@Typer.command()
def get_package_created():
    courier.Courier().get_package_created()

@Typer.command()
def help(args, get_test=False):
    courier.Courier.proc_args(args, get_test)


    

