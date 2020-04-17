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
import os
import questionary
from emrichen import Context, Template


class AppImageBuilderGenerator:
    def __init__(self):
        self.app_info_id = ''
        self.app_info_name = ''
        self.app_info_icon = ''
        self.app_info_version = ''
        self.app_info_exec = ''
        self.app_info_exec_args = ''
        
        self.runtime_env = []

        self.setup_questions()
        
    def setup_questions(self):
        # AppDir ->
        self.app_info_id = questionary.text('ID (com.example.app) :').ask()
        self.app_info_name = questionary.text('Application Name :').ask()
        self.app_info_icon = questionary.text('Icon :').ask()
        self.app_info_version = questionary.text('Version :').ask()
        self.app_info_exec = questionary.text('Executable path (usr/bin/app) :').ask()
        self.app_info_exec_args = questionary.text('Arguments [Default: $@] :').ask()

        # AppDir -> runtime
        questionary.select(
            'Generator (Select `Wrapper` if unsure)',
            choices=[
                'wrapper',
                'classic',
                'proot'
            ]).ask()

        while True:
            env = questionary.text('Runtime Environment Variable <Press Enter to break> :').ask()

            if len(env.strip()) == 0:
                break
            else:
                self.runtime_env.append(env)

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
        appimage_builder_yml_template_path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'template', 'AppImageBuilder.in.yml'))
        with open(appimage_builder_yml_template_path, 'r') as filedata:
            appimage_builder_yml_template = Template.parse(filedata, 'yaml')

        appimage_builder_yml_ctx = Context()

        logging.debug(appimage_builder_yml_template.render(appimage_builder_yml_ctx))

