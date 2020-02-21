# TIMEPAL

Cameron Merrick
Optiv
02.21.2020

## Overview

As an engineer, I find myself spending a lot of time in a CLI environment.  On the other hand, as a consultant I am expected to keep an accurate timelog of my activities for direct billing clients, as well as forecasting and project management.

### The Problem

Keeping track of the smaller tasks that might not have a calendar event to refer to when prepping my weekly timelog to submit.  Whether it be an unexpected call from a client, or a drive by request from a colleague to reboot a server, it's too easy for smaller ad-hoc tasks to slip through the cracks.

### The Solution

If there was some way to quickly mark down time without leaving the CLI, and without having to log into a new system, find my phone for 2FA, that could then dump all of the time entries from a date range I specify, that would make keeping track of time meaningfully easier for all those little 15 minute tasks that can add up to a significant amount of time over the course of a week, or month.

## Installation

- Download and extract the project or clone it using git. 
- (optional) toggle the virtual environment `source ./venv/bin/activate`
- Install with `pip install -e .` 

## Usage Options

### Command Syntax

`$ timepal log -c [client] -t [time] -m [message or notes]`

`
$ timepal dump -s [start-date] -e [end-date]`

### Examples

```$timepal log -c DIS -t 15 -m "modified Disney Phantom repo to allow read/write for everyone"``` 

`$ timepal log -c ADP -t 30 -m "prepped diagrams for Vault EaaS / Transit secrets engine"`

`$ timepal dump -s 2020-02-15 -e 2020-02-19`

