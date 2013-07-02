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

The following module is no mandatory but quite advised:
* blessings

Usage
===========
Type `./fetchLink.py {fetch,history,update} -h` for the manual

Configuring
==========

Configuring is (for now only) for programmers, even if quite easy and correctly splitted it remains quite obfustated in a lot of ways.

fetchLink
---------------
Main application

Modules
-------
* _Fetch_ : Main module, all the fetching is done here
* _Html_ : Constructing the result page
* _Parse_ : Argument parser all command line argument are processed here
* _Save_ : Saving the previous search to easily repeat them
* _Tools_ : The main tools and custom errors

Website
---------
Each website contain the custom tools to find the pictures it's webpages, forge the links to dl and so on.
