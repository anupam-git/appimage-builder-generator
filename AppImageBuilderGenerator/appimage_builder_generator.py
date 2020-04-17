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

import logging
from questionnaire import Questionnaire

class AppImageBuilderGenerator:
    def __init__(self):
        self.questionnaire = Questionnaire()
        self.setupQuestions()
        
    def setupQuestions(self):
        logging.debug("Setting up questions")
        self.questionnaire.one('day', 'Sunday', 'Monday', 'Tuesday', prompt='What day is it?')

        ### AppDir
        ## app_info
        # id
        # name
        # icon
        # version
        # exec
        # exec_args
        ## runtime
        # generator
        # env
        ## apt
        # arch
        # sources
        # include
        # exclude
        ## files
        # exclude
        ### AppImage
        ## arch
        ## file_name
        
    def generate(self):
        self.questionnaire.run()
        print(self.questionnaire.format_answers(fmt='array'))
