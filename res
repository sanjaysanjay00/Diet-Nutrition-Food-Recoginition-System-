"C:\Users\Fantasy solution\PycharmProjects\NutritionKerasCnn\venv\Scripts\python.exe" "C:/Users/Fantasy solution/PycharmProjects/NutritionKerasCnn/model.py"
2023-02-22 08:15:19.534617: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-02-22 08:15:19.535447: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
Found 6269 images belonging to 20 classes.
2023-02-22 08:15:28.875197: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-02-22 08:15:28.876871: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cublas64_11.dll'; dlerror: cublas64_11.dll not found
2023-02-22 08:15:28.878179: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cublasLt64_11.dll'; dlerror: cublasLt64_11.dll not found
2023-02-22 08:15:28.879245: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cufft64_10.dll'; dlerror: cufft64_10.dll not found
2023-02-22 08:15:28.880252: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'curand64_10.dll'; dlerror: curand64_10.dll not found
2023-02-22 08:15:28.881229: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cusolver64_11.dll'; dlerror: cusolver64_11.dll not found
2023-02-22 08:15:28.882302: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cusparse64_11.dll'; dlerror: cusparse64_11.dll not found
2023-02-22 08:15:28.884185: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudnn64_8.dll'; dlerror: cudnn64_8.dll not found
2023-02-22 08:15:28.884403: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1850] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2023-02-22 08:15:28.890964: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 198, 198, 16)      448

 max_pooling2d (MaxPooling2D  (None, 99, 99, 16)       0
 )

 conv2d_1 (Conv2D)           (None, 97, 97, 32)        4640

 max_pooling2d_1 (MaxPooling  (None, 48, 48, 32)       0
 2D)

 conv2d_2 (Conv2D)           (None, 46, 46, 64)        18496

 max_pooling2d_2 (MaxPooling  (None, 23, 23, 64)       0
 2D)

 conv2d_3 (Conv2D)           (None, 21, 21, 64)        36928

 max_pooling2d_3 (MaxPooling  (None, 10, 10, 64)       0
 2D)

 conv2d_4 (Conv2D)           (None, 8, 8, 64)          36928

 max_pooling2d_4 (MaxPooling  (None, 4, 4, 64)         0
 2D)

 flatten (Flatten)           (None, 1024)              0

 dense (Dense)               (None, 128)               131200

 dense_1 (Dense)             (None, 20)                2580

=================================================================
Total params: 231,220
Trainable params: 231,220
Non-trainable params: 0
_________________________________________________________________
Epoch 1/30
WARNING:tensorflow:AutoGraph could not transform <function Model.make_train_function.<locals>.train_function at 0x0000027B50E985E8> and will run it as-is.
Please report this to the TensorFlow team. When filing the bug, set the verbosity to 10 (on Linux, `export AUTOGRAPH_VERBOSITY=10`) and attach the full output.
Cause: 'arguments' object has no attribute 'posonlyargs'
To silence this warning, decorate the function with @tf.autograph.experimental.do_not_convert
195/195 [==============================] - 151s 764ms/step - loss: 2.8058 - accuracy: 0.1219
Epoch 2/30
195/195 [==============================] - 147s 752ms/step - loss: 2.5369 - accuracy: 0.2217
Epoch 3/30
195/195 [==============================] - 157s 802ms/step - loss: 2.2839 - accuracy: 0.3001
Epoch 4/30
195/195 [==============================] - 152s 781ms/step - loss: 2.0560 - accuracy: 0.3686
Epoch 5/30
195/195 [==============================] - 149s 765ms/step - loss: 1.8796 - accuracy: 0.4254
Epoch 6/30
195/195 [==============================] - 154s 789ms/step - loss: 1.7056 - accuracy: 0.4842
Epoch 7/30
195/195 [==============================] - 161s 821ms/step - loss: 1.5355 - accuracy: 0.5289
Epoch 8/30
195/195 [==============================] - 160s 814ms/step - loss: 1.3674 - accuracy: 0.5751
Epoch 9/30
195/195 [==============================] - 156s 796ms/step - loss: 1.1934 - accuracy: 0.6316
Epoch 10/30
195/195 [==============================] - 155s 794ms/step - loss: 1.0184 - accuracy: 0.6784
Epoch 11/30
195/195 [==============================] - 159s 812ms/step - loss: 0.8656 - accuracy: 0.7255
Epoch 12/30
195/195 [==============================] - 160s 820ms/step - loss: 0.7314 - accuracy: 0.7683
Epoch 13/30
195/195 [==============================] - 155s 794ms/step - loss: 0.5676 - accuracy: 0.8164
Epoch 14/30
195/195 [==============================] - 160s 818ms/step - loss: 0.4629 - accuracy: 0.8520
Epoch 15/30
195/195 [==============================] - 134s 687ms/step - loss: 0.3730 - accuracy: 0.8806
Epoch 16/30
195/195 [==============================] - 138s 708ms/step - loss: 0.2997 - accuracy: 0.9027
Epoch 17/30
195/195 [==============================] - 126s 647ms/step - loss: 0.2791 - accuracy: 0.9169
Epoch 18/30
195/195 [==============================] - 128s 658ms/step - loss: 0.2419 - accuracy: 0.9293
Epoch 19/30
195/195 [==============================] - 128s 658ms/step - loss: 0.2323 - accuracy: 0.9371
Epoch 20/30
195/195 [==============================] - 124s 632ms/step - loss: 0.1816 - accuracy: 0.9450
Epoch 21/30
195/195 [==============================] - 125s 643ms/step - loss: 0.1839 - accuracy: 0.9437
Epoch 22/30
195/195 [==============================] - 122s 627ms/step - loss: 0.1752 - accuracy: 0.9455
Epoch 23/30
195/195 [==============================] - 127s 650ms/step - loss: 0.1611 - accuracy: 0.9519
Epoch 24/30
195/195 [==============================] - 117s 600ms/step - loss: 0.1661 - accuracy: 0.9505
Epoch 25/30
195/195 [==============================] - 120s 613ms/step - loss: 0.1440 - accuracy: 0.9583
Epoch 26/30
195/195 [==============================] - 124s 637ms/step - loss: 0.1346 - accuracy: 0.9596
Epoch 27/30
195/195 [==============================] - 121s 617ms/step - loss: 0.1503 - accuracy: 0.9569
Epoch 28/30
195/195 [==============================] - 124s 637ms/step - loss: 0.1300 - accuracy: 0.9582
Epoch 29/30
195/195 [==============================] - 128s 654ms/step - loss: 0.1145 - accuracy: 0.9658
Epoch 30/30
195/195 [==============================] - 122s 624ms/step - loss: 0.1322 - accuracy: 0.9631

Process finished with exit code 0
