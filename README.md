fetchLink
=========

Fetch all pictures links in a picture browsing website (safebooru/gelbooru/danbooru...)

Some tags can be provided to refine the search, this script is mainly aimed for admins/moderators in order to ease up their task.


Installing
==========

You'll need either pip or easy_install in order to get the following python packages:
* html5lib
* beautifulsoup4
* requests

Usage
===========
  `fetchLink.py [-h] [--start START] [--find FIND] [--name NAME]
                    [--check-links] [--verbose] [--website WEBSITE]
                    [--admin-tools] [--fetch-pictures] [--fetch-thumbnails]
                    {fetch,show,update,repeat} nb_pages [tags [tags ...]]`

Fetch all the pages from the first one to <nb_pages>, according to the tag(s) provided
The following options are optionals: 
* `--start / -s START` : the script will start at <START> instead of first page
* `--find FIND` : the script will stop when finding the picture <FIND>
* `--name NAME` : custom naminging (you can use {tags}, {start} and {stop})
* `--check-links` : Check if the picture actually exists before adding it
* `--website WEBSITE` : Pick a website to fetch from
* `--admin-tools` : Add the admin tools (if available)
* `--fetch-pictures` : Fetch the pictures and save them in a folder (NotYetImplemented)
* `--fetch-thumbnails` : Fetch the thumbs and save them in a folder (NotYetImplemented)
* `--verbose / -v` : Increase verbosity (1: help - 2: debug)
Configuring
==========

Configuring is (for now only) for programmers, even if quite easy and correctly splitted it remains quite obfustated in a lot of ways.

fetchLink
---------------
Main application

Html
---------------
Constructing the result page

Parse
---------------
Argument parser, simple, ugly but working

Tools
---------------
The tools to find the pictures in webpages, forge the links to dl and so on.

