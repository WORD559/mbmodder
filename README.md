# mbmodder
Mount and Blade: Warband config/module editor

[![Maintainability](https://api.codeclimate.com/v1/badges/21c15b8fd2c6a7684331/maintainability)](https://codeclimate.com/github/WORD559/mbmodder/maintainability) [![Issue Count](https://codeclimate.com/github/WORD559/mbmodder/badges/issue_count.svg)](https://codeclimate.com/github/WORD559/mbmodder)

This is a modular CLI tool to allow simple modification of Mount and Blade: Warband. Game mods can be easily created and added and command line bindings will be automatically generated for new mods, allowing external developers the freedom to make their own tweaks.

## Installation ##

Requires `docopt`.

```
$ sudo pip install docopt
```

With `docopt` installed, simply clone the repository.

```
$ git clone https://github.com/WORD559/mbmodder.git
```

## Usage ##

Simply run `mbmodder.py`, on Linux this should be possible from bash but Windows users will have to execute it with Python on cmd.

```
$ ./mbmodder.py -h
```

This will list all available mods and their required arguments.
