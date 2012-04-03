#!/usr/bin/python2.6
"""
This is the heir apparent to the currently Ocamly castle-cli.
"""

import cmd
import sys
import logging
import os

castle_cli_log = logging.getLogger('castle_cli')
castle_cli_ch = logging.StreamHandler()
castle_cli_ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(module)s: %(message)s')
castle_cli_ch.setFormatter(formatter)
castle_cli_log.addHandler(castle_cli_ch)
castle_cli_ch = None

try:
    from acunu import castle
except ImportError:
    castle_cli_log.critical("Cannot find module acunu (hint: run this only on an Acunu box)")
    sys.exit(-1)
except Exception, e:
    castle_cli_log.critical("Failed due to excteption {0} of type {1}".format(e, type(e)))
    sys.exit(-1)

try:
    micasa = castle.Castle() #micasa will be the castle object through which all ops will go
except castle.CastleConnectionException:
    castle_cli_log.critical("Cannot make connection (hint: is Castle running?)")
    sys.exit(-1)
except Exception, e:
    castle_cli_log.critical("Failed due to exception {0} of type {1}".format(e, type(e)))
    sys.exit(-1)

class CastleCli(cmd.Cmd):
    """Castle cli command processor. """

    prompt = 'Castle:> '
    intro = 'Acunu Castle interactive shell.'
    last_output = ''
    current_collection = None #there can be only one (at any given time)

    def do_shell(self, line):
        "Run a shell command"
        castle_cli_log.info("running shell command: {0}".format(line))
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_create(self, name):
        """Create and attach to a new vertree."""
        try:
            if self.current_collection is not None:
                castle_cli_log.warn("Already attached; you should detach first.")
                return
            self.current_collection = micasa.collection_create(str(name))
            self.prompt = 'Castle/{0}:> '.format(str(name))
        except Exception, e:
            castle_cli_log.error("Failed due to exception {0} of type {1}".format(e, type(e)))
            sys.exit(-1)

    def do_attach(self, version_id, name):
        """Create an attachment to a given version number."""
        raise Exception('TODO')
        self.prompt = 'Castle/{0}:> '.format(coll_name)

    def do_detach(self, line):
        """Detach the current collection; this will remove the attachment in Castle."""
        if self.current_collection is None:
            castle_cli_log.warn("Not attached, can't detach.")
            return
        self.current_collection.detach()
        self.current_collection = None
        self.prompt = 'Castle:> '

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    CastleCli().cmdloop(intro="[Note: This is a work-in-progress and is opportunistically developed (i.e. we only integrate an interface if we need it). Most things are missing; either flesh it out yourself or nag TR to do it.]")

