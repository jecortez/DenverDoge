"""Code to pull data from Petfinder using the petpy module.

Example usage:
    >>> python pull_petfinder_data.py pull-colorado-data --pages 1 --outfile animals.csv

To this code, you'll need to do these things:
    1. Get a Petfinder API Key and Secret.
        - Create a Petfinder account.
        - Go to this page and click "Get an API key": https://www.petfinder.com/developers/
        - After creating them, your keys will be here: https://www.petfinder.com/user/developer-settings/
    2. Install petpy, click, pandas, and requests.

Notes:
    - If you don't wish to have your API credentials in this code, you can store them in a
      separate credentials file, or as environment variables.
    - petpy links:
        - Documentation: https://petpy.readthedocs.io/en/latest/
        - GitHub: https://github.com/aschleg/petpy

"""

import click

import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import requests
from urllib.parse import urljoin

import petpy

API_KEY = 'YOUR-API-KEY-HERE'
API_SECRET = 'YOUR-API-SECRET-HERE'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--pages', default=1, type=int, help='How many pages to pull (with 100 results per page)')
@click.option('--outfile', type=str, required=True, help='How many pages to pull (with 100 results per page)')
def pull_colorado_data(pages, outfile):
    pf = petpy.Petfinder(key=API_KEY, secret=API_SECRET)
    print(f'pulling {pages} page(s) from Petfinder')
    animals = pf.animals(results_per_page=100, pages=pages, return_df=True, location='CO')

    print(f'saving data to {outfile}')
    animals.to_csv(outfile, index=False)

if __name__ == '__main__':
    cli()
