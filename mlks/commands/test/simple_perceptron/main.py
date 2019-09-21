# Machine Learning Keras Suite
#
# A Python submodule that trains a simple perceptron.
#
# Author: Björn Hempel <bjoern@hempel.li>
# Date:   19.09.2019
# Web:    https://github.com/bjoern-hempel/machine-learning-keras-suite
#
# LICENSE
#
# MIT License
#
# Copyright (c) 2019 Björn Hempel <bjoern@hempel.li>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click

from mlks.commands.main import Command


class SimplePerceptron(Command):

    def __init__(self, general_config, machine_learning_config):
        self.general_config = general_config
        self.machine_learning_config = machine_learning_config

        # initialize the parent class
        super().__init__()

    def do(self):
        if not self.is_config_correct(self.machine_learning_config):
            return

        # start the timer
        self.start_timer('train')
        self.start_timer('train2')

        verbose = self.general_config.verbose

        click.echo('SimplePerceptron')

        # finish the timer
        self.finish_timer('train')