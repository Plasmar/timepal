#############################################################################
#############################################################################
#   FILENAME    :   timepal.py
#   AUTHOR      :   cameron merrick
#   DATE        :   02.20.2020
#   LICENSE     :   N/A
#   DESCRIPTION :   command line utility for quick ad-hoc time logging
#############################################################################
#############################################################################


import csv
import os
import click
import datetime
from tabulate import tabulate
import pandas as pd

# Set up the datetime object for creating filenames
now = datetime.date.today()
nowstr = str(now) + '.csv'


@click.group()
def cli():
    pass

@click.command()
@click.option('--outfile', '-o', default=nowstr)
@click.option('--client', '-c', required=True, type=str)
@click.option('--timelog', '-t', required=True, type=int)
@click.option('--message', '-m', default="...", type=str)
def log(outfile, client, timelog, message):
    """
    [*] Read timelog input from stdin and write to a text file...

    """

    # check to see if the outfile is invalid / !exists
    data_file = os.path.join('data/', outfile)
    if os.path.isfile(data_file):
        print("[*] Logging {} minutes of time for client: {}.".format(timelog, client))
        with open('data/' + outfile, 'a') as f:
            f.write(client + ',' + str(timelog) + ',' + message + '\n')


    else:
        print("[*] Creating file for {}".format(os.path.splitext(outfile)[0]) + '...\n')
        print("[*] Success!\n")
        print("[*] Logging {} minutes of time for client: {}.".format(timelog, client))
        with open('data/' + outfile, 'a') as f:
            f.write(client + ',' + str(timelog) + ',' + message + '\n')

# Aggregate a time period (e.g. 1 week) and render to user for adding to OpenAir
@click.command()
@click.option('--start', '-s', required=True, help='[*] inclusive date FROM (yyyy-mm-dd)')
@click.option('--end', '-e', required=True, help='[*] inclusive date END (yyyy-mm-dd)')
def dump(start, end):
    """
    [*] Reads start/end dates from stdin and renders a timelog summary report.

    """
    sdate = datetime.date.fromisoformat(start)
    edate = datetime.date.fromisoformat(end)

    delta = edate - sdate

    for i in range(delta.days + 1):
        iter_day = sdate + timedelta(days=i)
        if not os.path.isfile('data/' + iter_file):
            print("\n[*] No data for  " + iter_file +'\n')
            continue
        df = pd.read_csv(iter_file)
        print(tabulate(df, tablefmt='psql')


        # with open('data/' + str(start) + '.csv', 'r') as readfile:
            # reader = csv.reader(readfile)
            # for row in reader:
                # print(row)

# Add the two subcommands to the Click group formed at the top
cli = click.CommandCollection(sources=[log, dump])

if __name__ == '__main__':
    cli()
