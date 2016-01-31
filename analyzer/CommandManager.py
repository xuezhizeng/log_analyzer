#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import sys
from grep import (grep,
                  result_parser)

CONFIG_PATH = os.path.join(os.path.abspath(os.curdir),
                           'config.ini')
DOCUMENT = ''
CONFIG_FORMAT = """
            [regex]
            regex = (?P<date>\S*)\s(?P<time>\S*)\s(?P<action>\S*)\s(?P<path>\S*)\s(?P<file>\S*)
            labels = date time action path file
            [path]
            log_path = default.log
            """


class BaseManager(object):
    """
    BaseManager of the CommandManager, mainly to make a singleton.
    """
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(BaseManager, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class CommandManager(BaseManager):
    """
    CommandManager to handle commands from the client.
    """
    __all__ = ['search', 'setregex', 'help', 'getlabels', 'setpath',
               'getregex', 'getpath',  'clear', 'setlabels']

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(CONFIG_PATH)
        try:
            self.log_path = self.config.get('path', 'log_path')
            self.regex = self.config.get('regex', 'regex')
            self.labels = self.config.get('regex', 'labels').split()
        except ConfigParser.NoSectionError:
            print "Can't find config.ini !!!"
            print """
            config.ini should in fomat below!
            {config_format}
            """.format(config_format=CONFIG_FORMAT)
            sys.exit()

    def search(self, args):
        """::help::
        search logs matches the kewword.
        example:
        >>> search CREATE,ISDIR
        >>> 12:00 CREATE LOG1(too long too show you in help)
        >>> 12:01 DELETE LOG2
        :param args: keyword in log
        """
        if self.log_path == '':
            print 'Set path first!!!'
            return
        if len(args) == 0:
            print 'Plearse enter the keyword!!!'
            return
        keyword = '\b'.join(args)
        for log in result_parser(self.regex, self.labels,
                                 grep(self.log_path, keyword)):
            print (' '*5).join(log)

    def help(self, args):
        """::help::
        get help instruction.
        example:
        >>> help function -> how to use function
        >>> help -> all the instruction desplayed
        """
        if len(args) == 0:
            for func in self.__all__:
                print getattr(self, func).__name__
                print getattr(self, func).__doc__
        else:
            for func in args:
                print getattr(self, func).__doc__

    def setpath(self, args):
        """::help::
        set log path by simply type path in commandline
        example:
        >>> ../../test.log
        >>> set log path: ../../test.log
        """
        self.config.set('path', 'log_path', args)
        self.config.write(open(CONFIG_PATH, "w"))
        self.log_path = self.config.get('path', 'log_path')
        print 'set log path: ' + self.log_path

    def getpath(self, args):
        """::help::
        print path in commandline
        """
        print self.log_path

    def setregex(self, args):
        """::help::
        set regex expression in commandline
        example:
        >>> setregex (?P<date>\S*)\s(?P<time>\S*)\s(?P<action>\S*)\s(?P<path>\S*)\s(?P<file>\S*)
        >>> set regex expression: (?P<date>\S*)\s(?P<time>\S*)\s(?P<action>\S*)\s(?P<path>\S*)\s(?P<file>\S*)
        """
        self.config.set('regex', 'regex', args)
        self.config.write(open(CONFIG_PATH, "w"))
        self.regex = self.config.get('regex', 'regex')
        print 'set regex expression: ' + self.regex

    def getregex(self, args):
        """::help::
        print regex expression in commandline
        """
        print self.regex

    def setlabels(self, args):
        """::help::
        set labels corresponding to the regex expression.
        example:
        >>> setlabels date time action path file
        >>> set labels: date time action path file
        """
        self.config.set('regex', 'labels', args)
        self.config.write(open(CONFIG_PATH, "w"))
        self.labels = self.config.get('regex', 'labels').split()
        print 'set labels: ' + self.labels

    def getlabels(self, args):
        """::help::
        print labels corresponding to the regex expression
        """
        print self.labels

    def clear(self, args):
        """::help::
        clear your screen
        example:
        >>> clear
        """
        os.system('clear')

