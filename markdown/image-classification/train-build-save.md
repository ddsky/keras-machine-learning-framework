# Train, build and save the model

...

## Train, build and save the model

The data set `./data/raw/flowers` is based on Kaggle's floral data set: https://www.kaggle.com/alxmamaev/flowers-recognition. The following command trains the specified data folder `./data/raw/flowers` and writes the calculated model to `./data/inceptionv3-trained.h5`.

```bash
(keras-gpu) C:\Users> ml train --data-path=./data/raw/flowers --model-file=./data/inceptionv3-trained.h5
Using TensorFlow backend.

general
-------
verbose:                  False
debug:                    False

transfer_learning
-----------------
data_path:                ./Data/raw/flowers
transfer_learning_model:  InceptionV3
number_trainable_layers:  305
input_dimension:          299
dense_size:               512
dropout:                  0.5
weights:                  imagenet

machine_learning
----------------
model_file:               ./Data/inceptionv3-trained.h5
model_config:             ./Data/inceptionv3-trained.json
epochs:                   10
learning_rate:            0.001
activation_function:      tanh
loss_function:            mean_squared_error
optimizer:                adam
metrics:                  accuracy
environment_path:         None


Are these configurations correct? Continue? [Y/n] y
```

A time overview and graphic can be found on the CPU/GPU comparison page: [GPU vs CPU](/markdown/hardware/gpu-vs-cpu.md)

### @NVIDIA GeForce GTX 1060 6GB (Desktop)

```bash
...
Epoch 1/10
135/135 [==============================] - 55s 405ms/step - loss: 0.8413 - acc: 0.6882
Epoch 2/10
135/135 [==============================] - 26s 195ms/step - loss: 0.5610 - acc: 0.7954
Epoch 3/10
135/135 [==============================] - 26s 190ms/step - loss: 0.4741 - acc: 0.8235
Epoch 4/10
135/135 [==============================] - 26s 190ms/step - loss: 0.4466 - acc: 0.8337
Epoch 5/10
135/135 [==============================] - 27s 196ms/step - loss: 0.3825 - acc: 0.8639
Epoch 6/10
135/135 [==============================] - 27s 202ms/step - loss: 0.4184 - acc: 0.8466
Epoch 7/10
135/135 [==============================] - 34s 252ms/step - loss: 0.3591 - acc: 0.8711
Epoch 8/10
135/135 [==============================] - 26s 192ms/step - loss: 0.3598 - acc: 0.8771
Epoch 9/10
135/135 [==============================] - 29s 213ms/step - loss: 0.3258 - acc: 0.8762
Epoch 10/10
135/135 [==============================] - 28s 207ms/step - loss: 0.3448 - acc: 0.8758

--- time measurement for "preparations": 17.5051s ---

--- time measurement for "fit": 303.5375s ---

--- time measurement for "save model": 33.7900s ---
```

### @NVIDIA GeForce GT 750M 2GB (Notebook)

```bash
...
Epoch 1/10
135/135 [==============================] - 233s 2s/step - loss: 0.8411 - acc: 0.6910
Epoch 2/10
135/135 [==============================] - 236s 2s/step - loss: 0.5703 - acc: 0.7919
Epoch 3/10
135/135 [==============================] - 238s 2s/step - loss: 0.4762 - acc: 0.8242
Epoch 4/10
135/135 [==============================] - 238s 2s/step - loss: 0.4377 - acc: 0.8385
Epoch 5/10
135/135 [==============================] - 244s 2s/step - loss: 0.3846 - acc: 0.8646
Epoch 6/10
135/135 [==============================] - 245s 2s/step - loss: 0.4335 - acc: 0.8407
Epoch 7/10
135/135 [==============================] - 244s 2s/step - loss: 0.3623 - acc: 0.8741
Epoch 8/10
135/135 [==============================] - 245s 2s/step - loss: 0.3620 - acc: 0.8743
Epoch 9/10
135/135 [==============================] - 256s 2s/step - loss: 0.3369 - acc: 0.8773
Epoch 10/10
135/135 [==============================] - 236s 2s/step - loss: 0.3477 - acc: 0.8793

--- time measurement for "preparations": 18.3966s ---

--- time measurement for "fit": 2415.0062s ---

--- time measurement for "save model": 29.7956s ---     
```

### @Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz (Single Core) - MacOS

```bash
Epoch 1/10
135/135 [==============================] - 659s 5s/step - loss: 0.8175 - acc: 0.6991
Epoch 2/10
135/135 [==============================] - 641s 5s/step - loss: 0.5490 - acc: 0.7976
Epoch 3/10
135/135 [==============================] - 639s 5s/step - loss: 0.4698 - acc: 0.8268
Epoch 4/10
135/135 [==============================] - 640s 5s/step - loss: 0.4399 - acc: 0.8417
Epoch 5/10
135/135 [==============================] - 636s 5s/step - loss: 0.3821 - acc: 0.8625
Epoch 6/10
135/135 [==============================] - 635s 5s/step - loss: 0.3999 - acc: 0.8526
Epoch 7/10
135/135 [==============================] - 636s 5s/step - loss: 0.3524 - acc: 0.8750
Epoch 8/10
135/135 [==============================] - 638s 5s/step - loss: 0.3414 - acc: 0.8812
Epoch 9/10
135/135 [==============================] - 632s 5s/step - loss: 0.3261 - acc: 0.8829
Epoch 10/10
135/135 [==============================] - 638s 5s/step - loss: 0.3445 - acc: 0.8774

--- time measurement for "preparations": 19.0787s ---

--- time measurement for "fit": 6393.7390s ---

--- time measurement for "save model": 41.3459s ---
```

### @Intel(R) Core(TM) i7-4712HQ CPU @ 2.30GHz (Single Core) - Windows

```bash
...
Epoch 1/10
135/135 [==============================] - 948s 7s/step - loss: 0.8142 - acc: 0.6942
Epoch 2/10
135/135 [==============================] - 902s 7s/step - loss: 0.5621 - acc: 0.7942
Epoch 3/10
135/135 [==============================] - 870s 6s/step - loss: 0.4704 - acc: 0.8281
Epoch 4/10
135/135 [==============================] - 873s 6s/step - loss: 0.4600 - acc: 0.8223
Epoch 5/10
135/135 [==============================] - 908s 7s/step - loss: 0.3833 - acc: 0.8616
Epoch 6/10
135/135 [==============================] - 885s 7s/step - loss: 0.4216 - acc: 0.8456
Epoch 7/10
135/135 [==============================] - 933s 7s/step - loss: 0.3589 - acc: 0.8748
Epoch 8/10
135/135 [==============================] - 915s 7s/step - loss: 0.3564 - acc: 0.8741
Epoch 9/10
135/135 [==============================] - 898s 7s/step - loss: 0.3401 - acc: 0.8731
Epoch 10/10
135/135 [==============================] - 884s 7s/step - loss: 0.3475 - acc: 0.8760

--- time measurement for "preparations": 16.8698s ---

--- time measurement for "fit": 9016.7745s ---

--- time measurement for "save model": 28.6788s ---
```

### Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (Single Core) - Windows

```bash
...
135/135 [==============================] - 2586s 19s/step - loss: 0.8425 - acc: 0.6845
Epoch 2/10
135/135 [==============================] - 2544s 19s/step - loss: 0.5630 - acc: 0.7936
Epoch 3/10
135/135 [==============================] - 2511s 19s/step - loss: 0.4737 - acc: 0.8254
Epoch 4/10
135/135 [==============================] - 2488s 18s/step - loss: 0.4387 - acc: 0.8361
Epoch 5/10
135/135 [==============================] - 2516s 19s/step - loss: 0.3825 - acc: 0.8637
Epoch 6/10
135/135 [==============================] - 2515s 19s/step - loss: 0.4168 - acc: 0.8427
Epoch 7/10
135/135 [==============================] - 2512s 19s/step - loss: 0.3707 - acc: 0.8700
Epoch 8/10
135/135 [==============================] - 2517s 19s/step - loss: 0.3599 - acc: 0.8713
Epoch 9/10
135/135 [==============================] - 2492s 18s/step - loss: 0.3429 - acc: 0.8701
Epoch 10/10
135/135 [==============================] - 2502s 19s/step - loss: 0.3526 - acc: 0.8739

--- time measurement for "preparations": 16.2699s ---

--- time measurement for "fit": 25183.4061s ---

--- time measurement for "save model": 28.3226s ---
```

## JSON config format

```json
{
    "environment": {
        "classes": [
            "daisy",
            "dandelion",
            "rose",
            "sunflower",
            "tulip"
        ],
        "measurement": {
            "fit": 12345,
            "preparation": 987
        }
    },
    "general": {
        "debug": false,
        "verbose": true
    },
    "machine_learning": {
        "activation_function": "tanh",
        "environment_path": null,
        "epochs": 10,
        "learning_rate": 0.001,
        "loss_function": "mean_squared_error",
        "metrics": "accuracy",
        "model_config": "./Data/inceptionv3-trained.json",
        "model_file": "./Data/inceptionv3-trained.h5",
        "optimizer": "adam"
    },
    "transfer_learning": {
        "data_path": "./Data/raw/flowers",
        "dense_size": 512,
        "dropout": 0.5,
        "input_dimension": 299,
        "number_trainable_layers": 305,
        "transfer_learning_model": "InceptionV3",
        "weights": "imagenet"
    }
}
```

## A. Further Tutorials

* [An introduction to artificial intelligence](https://github.com/friends-of-ai/an-introduction-to-artificial-intelligence)

## B. Sources

* ...

## C. Authors

* Björn Hempel <bjoern@hempel.li> - _Initial work_ - [https://github.com/bjoern-hempel](https://github.com/bjoern-hempel)

## D. License

This tutorial is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details

## E. Closing words

Have fun! :)

