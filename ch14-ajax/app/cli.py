import os
import click
from app import app

current_directory = os.environ['FLASK_APP'].split('/')[0]+'/'


@app.cli.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F' + current_directory+'babel.cfg -k _l -o '+current_directory+'messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i'+ current_directory+'messages.pot -d '+ current_directory+'app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove(current_directory+'messages.pot')


@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F' + current_directory+'babel.cfg -k _l -o '+current_directory+'messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel update -i '+ current_directory+'messages.pot -d '+ current_directory+'app/translations'):
        raise RuntimeError('update command failed')
    os.remove(current_directory+'messages.pot')


@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d' + current_directory +'app/translations'):
        raise RuntimeError('compile command failed')
