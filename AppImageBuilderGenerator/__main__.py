#!/usr/bin/env python3
#  Copyright 2020 Anupam Basak <anupam.basak27@gmail.com>
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.

import argparse
import logging
import os
from AppImageBuilderGenerator import AppImageBuilderGenerator

def __main__():
    parser = argparse.ArgumentParser(description='AppImageBuilder Recipe Generation tool')
    parser.add_argument('--log', dest='loglevel', default="INFO",
                        help='logging level <CRITICAL | ERROR | WARNING | INFO(default) | DEBUG>')
    
    args = parser.parse_args()
    numeric_level = getattr(logging, args.loglevel.upper())
    if not isinstance(numeric_level, int):
        logging.error('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=numeric_level)

    generator = AppImageBuilderGenerator()
    generator.generate()
    

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    __main__()
