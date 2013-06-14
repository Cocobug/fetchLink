fetchLink
=========

Fetch all pictures links in a website


Installing
==========

You'll need either pip or easy_install in order to get the following python packages:
* html5lib
* beautifulsoup4
* requests

Usage
===========
  `./fetchLink <nbPagesToFetch> <listOfTags> [#imageMax] [&pageToStartWith]`

Configuring
==========

Configuring is (for now only) for programmers, even if quite easy and correctly splitted it remains quite obfustated in a lot of ways.

fetchLink
---------------

Main application

Html
---------------
The website to get, the methods to construct the result page

Parse
---------------
Argument parser

Tools
---------------
The tools to find the pictures in webpages, forge the links to dl and so on.

