# Toolkit

My toolkit project, write some tools or code snippets for fun and practice.

| Index | Brief Introduction |
| ----- | ------------------ |
| [Cheat Sheet](https://github.com/LyleMi/toolkit#cheatsheet) | A simple, extensible command line cheat sheet |
| [DB Wrapper](https://github.com/LyleMi/toolkit#dbwrapper) | Database Wrapper which makes Database cursor API easier to use. |
| [Miscellaneous](https://github.com/LyleMi/toolkit#miscellaneous) | A variety of scripts, including modifying the system Mac, getting the current Wifi password, command line dictionary, and more. |
| [Operations](https://github.com/LyleMi/toolkit#operations) | Operations scripts for configure server. |
| [Sublime](https://github.com/LyleMi/toolkit#sublime) | Some Sublime code snippet and config file. |

## Cheat sheet

A simple, extensible command line cheat sheet which contains:

- Common compress command for multiple suffix
- Git config / log / tag / ...
- IPtables Set / List / Delete
- Common Linux Command
- MySQL Query
- Python Environment Configuration
- Reverse Shell command
- SSH Configuration


```sh
# Usage
python cheat.py <category> [ <keyword> | <arguments> ]
```

## DBWrapper

Some database wrappers for ElasticSearch / MongoDB / PostgreSQL / MySQL / SQLite. Make Database cursor API easier to use.

> Example

```python
opts = {
    "host": "localhost",
    "user": "root",
    "pwd": "password",
    "db": "database"
}

# init database
db = DB(opts)
print(db.showDBs())
print(db.showTables())

# raw execute
db.cur.execute("delete from user")
sql = "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"

# insert single data
db.insert(sql, ['admin', 'admin'])

# insert multiple data
db.insert(sql, [['2', '3'], ['4', '5']], True)

# select
sql = "SELECT * FROM user WHERE username = %s"
print(db.select(sql, 'admin'))
sql = "SELECT * FROM user"
print(db.select(sql))
```

## Miscellaneous

### ChangeMac

A script for change mac address which works on Windows / Mac OS.

```python
usage: [options]

Tool For Change Mac Address

optional arguments:
  -h, --help            show this help message and exit
  -m mac, --mac mac     mac address
  -i interface, --interface interface
                        network interface
  -d desc, --desc desc  network interface des
```

### Colorize

A library for colorize text.

![image](https://raw.githubusercontent.com/LyleMi/toolkit/images/colorize.png)

### DNS Rebinding

A mini DNS rebinding server, it's easy to custom.

### Flask Seed

A script for flask quick start.

### getwifipwd

Get current wifi password, works on Windows / Mac OS / Linux.

### path diff

Tool used to monitor file changes.

```
usage: pathdiff.py [options]

simple path diff tool

optional arguments:
  -h, --help            show this help message and exit
  -i, --init            initial at this path
  -f first, --first first
                        first path file to diff
  -s second, --second second
                        second path file to diff
  -p, --persistent      run in persistent mode
  -t TIMESLEEP, --timesleep TIMESLEEP
                        set sleeptime

A simple path diff tool
```

### minijump

A mini dir jump tool for Windows.

```
# add shortcut
python minijump.py a [short] [fullpath]

# delete shortcut
python minijump.py d [short]

# list shortcut
python minijump.py l

# jump to
python minijump.py [short]
```

### Windbghelper

Script for debug Edge / IE.

### YD

Youdao dict command line tool.

![image](https://raw.githubusercontent.com/LyleMi/toolkit/images/youdao.png)

### Waf

Simple PHP Waf Framework.

## Operations

Operations scripts for configure server.

- config
    - .vimrc
- deploy script
    - cobra
    - gitlab
    - moloch
    - octopress
    - openvpn
    - supervisor
- install command
    - docker
    - java
    - penetration testing
- backup mysql

## Sublime

Some Sublime code snippet and config file. It contains PHP debug, python hash / logger / requests / ... , docker compose, etc. 
