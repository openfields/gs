#!/usr/bin/env python
#
##############################################################################
#
# MODULE:       model
#
# AUTHOR(S):    will
#               
# PURPOSE:      Script generated by wxGUI Graphical Modeler.
#
# DATE:         Fri Jun 24 20:51:12 2016
#
##############################################################################

#%module
#% description: Script generated by wxGUI Graphical Modeler.
#%end

import sys
import os
import atexit

from grass.script import parser, run_command

def cleanup():
    pass

def main():
    run_command("v.category",
                input = "b15_s100@will",
                layer = "1",
                type = "point,line,centroid,face",
                output = "out_nocat",
                option = "del",
                cat = -1,
                step = 1)

    run_command("v.category",
                input = "out_nocat",
                layer = "1",
                type = "point,line,centroid,face",
                output = "out_uniq",
                option = "add",
                cat = 1,
                step = 1)

    run_command("v.db.addtable",
                map = "out_uniq",
                layer = 1,
                key = "cat",
                columns = "cat integer, length double")

    run_command("v.to.db",
                map = "out_uniq",
                layer = "1",
                type = "point,line,boundary,centroid",
                option = "length",
                columns = "length",
                units = "meters",
                query_layer = "1",
                separator = "pipe")


    return 0

if __name__ == "__main__":
    options, flags = parser()
    atexit.register(cleanup)
    sys.exit(main())
