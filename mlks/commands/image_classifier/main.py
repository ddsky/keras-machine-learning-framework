# Machine Learning Keras Suite
#
# This is the basic image classifier class from which all train, evaluate and prepare classes inherit.
#
# Author: Björn Hempel <bjoern@hempel.li>
# Date:   02.10.2019
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
import os
import math

from mlks.commands.main import Command
from mlks.helper.filesystem import get_number_of_folders_and_files

from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input as InceptionV3PreprocessInput

from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input as ResNet50PreprocessInput

from keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import preprocess_input as VGG19PreprocessInput

from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.applications.inception_resnet_v2 import preprocess_input as InceptionResNetV2PreprocessInput

from keras.layers import Dense, GlobalAveragePooling2D, Dropout, Activation
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.optimizers import SGD

from keras.callbacks import LearningRateScheduler


class ImageClassifier(Command):

    def __init__(self, config):
        self.config = config

        # initialize the parent class
        super().__init__(config)

    def get_tl_model(self):
        transfer_learning_model = self.config.gettl('transfer_learning_model')

        if self.config.get('verbose'):
            click.echo('Use tl model "%s".' % transfer_learning_model)

        return getattr(self, 'get_tl_' + transfer_learning_model.lower())()

    def get_tl_inceptionv3(self):
        dim = self.config.gettl('input_dimension')
        weights = self.config.gettl('weights')
        return InceptionV3(weights=weights, include_top=False, input_shape=(dim, dim, 3))

    def get_tl_resnet50(self):
        dim = self.config.gettl('input_dimension')
        weights = self.config.gettl('weights')
        return ResNet50(weights=weights, include_top=False, input_shape=(dim, dim, 3))

    def get_tl_vgg19(self):
        dim = self.config.gettl('input_dimension')
        weights = self.config.gettl('weights')
        return VGG19(weights=weights, include_top=False, input_shape=(dim, dim, 3))

    def get_tl_inceptionresnetv2(self):
        dim = self.config.gettl('input_dimension')
        weights = self.config.gettl('weights')
        return InceptionResNetV2(weights=weights, include_top=False, input_shape=(dim, dim, 3))

    def load_image(self, path):
        if self.config.get('verbose'):
            click.echo('load image: %s' % self.config.gettl('transfer_learning_model'))
        return getattr(self, 'load_image_' + self.config.gettl('transfer_learning_model').lower())(path)

    def load_image_inceptionv3(self, path):
        image = load_img(
            path,
            target_size=(self.config.gettl('input_dimension'), self.config.gettl('input_dimension'))
        )
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        return InceptionV3PreprocessInput(image)

    def load_image_resnet50(self, path):
        image = load_img(
            path,
            target_size=(self.config.gettl('input_dimension'), self.config.gettl('input_dimension'))
        )
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        return ResNet50PreprocessInput(image)

    def load_image_vgg19(self, path):
        image = load_img(
            path,
            target_size=(self.config.gettl('input_dimension'), self.config.gettl('input_dimension'))
        )
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        return VGG19PreprocessInput(image)

    def load_image_inceptionresnetv2(self, path):
        image = load_img(
            path,
            target_size=(self.config.gettl('input_dimension'), self.config.gettl('input_dimension'))
        )
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        return InceptionResNetV2PreprocessInput(image)

    def get_preprocessing_function_inceptionv3(self):
        return InceptionV3PreprocessInput

    def get_preprocessing_function_resnet50(self):
        return ResNet50PreprocessInput

    def get_preprocessing_function_vgg19(self):
        return VGG19PreprocessInput

    def get_preprocessing_function_inceptionresnetv2(self):
        return InceptionResNetV2PreprocessInput

    def get_model(self):
        number_trainable = self.config.gettl('number_trainable_layers')
        dense_size = self.config.gettl('dense_size')
        dropout = self.config.gettl('dropout')
        categories = self.get_categories()
        activation = 'relu'

        # get the transfer learning model
        base_model = self.get_tl_model()

        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(dense_size, activation=activation)(x)
        x = Dropout(dropout)(x)

        if categories == 2:
            probabilities = Dense(1)(x)
            predictions = Activation('sigmoid')(probabilities)
        else:
            probabilities = Dense(categories)(x)
            predictions = Activation('softmax')(probabilities)

        model = Model(inputs=base_model.input, outputs=predictions)

        # set the first number_trainable layers of the network to be non-trainable
        number_not_trainable = len(model.layers) - number_trainable
        for layer in model.layers[:number_not_trainable]:
            layer.trainable = False
        for layer in model.layers[number_not_trainable:]:
            layer.trainable = True

        # compile model
        self.compile_model(model)

        return model

    def load_model(self, model_file):
        if self.config.get('verbose'):
            click.echo('load model: %s' % self.config.gettl('transfer_learning_model'))

        model = load_model(model_file)
        self.compile_model(model)

        return model

    def step_decay(self, epoch):
        initial_learning_rate = self.config.getml('learning_rate')
        drop = self.config.getml('learning_rate_drop')
        epochs_drop = self.config.getml('learning_rate_epochs_drop')
        return initial_learning_rate * math.pow(drop, math.floor(epoch / epochs_drop))

    def compile_model(self, model):
        if self.config.getml('optimizer') == 'sgd':
            learning_rate = self.config.getml('learning_rate')
            momentum = self.config.getml('momentum')
            decay = self.config.getml('decay')
            nesterov = self.config.getml('nesterov')
            optimizer = SGD(lr=learning_rate, momentum=momentum, decay=decay, nesterov=nesterov)
        else:
            optimizer = 'Adam'

        loss = self.config.getml('loss_function')
        metrics = self.config.getml('metrics')

        if self.config.get('verbose'):
            click.echo('Used optimizer: %s' % self.config.getml('optimizer'))
            click.echo('Loss: %s' % loss)
            click.echo('Metrics: %s' % metrics)
            if self.config.getml('optimizer') == 'sgd':
                click.echo('Learning rate: %s' % learning_rate)
                click.echo('Momentum: %s' % momentum)
                click.echo('Decay: %s' % decay)
                click.echo('Nesterov: %s' % nesterov)

        model.compile(optimizer=optimizer, loss=loss, metrics=[metrics])

    def get_image_generator(self):
        validation_split = self.config.getml('validation_split')

        if self.config.get('verbose'):
            click.echo('Validation split: %s' % validation_split)

        return ImageDataGenerator(
            preprocessing_function=getattr(
                self, 'get_preprocessing_function_' + self.config.gettl('transfer_learning_model').lower()
            )(),
            validation_split=validation_split
        )

    def get_train_generator(self, image_generator):
        dim = self.config.gettl('input_dimension')
        data_path = self.config.get_data('data_path')

        return image_generator.flow_from_directory(
            data_path,
            target_size=(dim, dim),
            color_mode='rgb',
            batch_size=32,
            class_mode='categorical',
            subset='training',
            shuffle=True
        )

    def get_validation_generator(self, image_generator):
        dim = self.config.gettl('input_dimension')
        data_path = self.config.get_data('data_path')

        return image_generator.flow_from_directory(
            data_path,
            target_size=(dim, dim),
            color_mode='rgb',
            batch_size=32,
            class_mode='categorical',
            subset='validation',
            shuffle=True
        )

    def train(self, model, train_generator, validation_generator):
        step_size_train = train_generator.n // train_generator.batch_size
        step_size_validation = validation_generator.n // validation_generator.batch_size
        epochs = self.config.getml('epochs')
        verbose = 1 if self.config.get('verbose') else 0

        learning_rate_scheduler = LearningRateScheduler(self.step_decay, verbose=verbose)
        return model.fit_generator(
            generator=train_generator,
            steps_per_epoch=step_size_train,
            validation_data=validation_generator,
            validation_steps=step_size_validation,
            epochs=epochs,
            verbose=verbose,
            callbacks=[learning_rate_scheduler]
        )

    def get_categories(self):
        # get some needed configuration parameters
        data_path = self.config.get_data('data_path')

        # check folder
        if not os.path.isdir(data_path):
            raise AssertionError('"%s" does not exists or seems not to be a folder.')

        data_path_info = get_number_of_folders_and_files(data_path)

        return data_path_info['folders']
