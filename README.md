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
  `./fetchLink <nbPagesToFetch> <listOfTags> [?imageMax] [%pageToStartWith] [@]`

Fetch all the pages from the first one to <nbPagesToFetch>, following the tag(s) <listOfTags>
The following options are optionals: 
* ?<idOfAPicture> : the script will stop when finding the picture <idOfAPicture>
* %<pageNumber> : the script will start at <pageNumber> instead of first page
* @<nb> : (<nb>=0) Check if the picture actually exists before adding it, (<nb>=1) check if the page referencing the picture actually exists

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

