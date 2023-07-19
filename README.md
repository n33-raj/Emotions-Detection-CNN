# Emotions-Detection-CNN

Built a Convolutional Neural Network (CNN) for emotion recognition using the Keras library with TensorFlow backend. This CNN model takes grayscale images of size 48x48 as input and aims to classify emotions into 7 classes. The dataset consists of a training set and a validation set.

Here's a summary of the steps taken in the code:

-Import the necessary libraries for building and training the CNN.
-Preprocess the training and test data using ImageDataGenerator with data augmentation for the training data (to improve generalization).
-Build the CNN model using models.Sequential() and add convolutional layers, max-pooling layers, dropout layers, and fully connected layers.
-Compile the CNN model with an Adam optimizer, categorical cross-entropy loss, and accuracy as a metric.
-Train the CNN model on the training set and evaluate it on the validation set using fit().
-Save the trained model to a file named 'Emotions-Model.h5'.
-Plot and save the training and validation loss/accuracy over epochs using Matplotlib.
-Setting up the CNN architecture, data preprocessing, and training. Training for 80 epochs might be sufficient.
- We can experiment with the number of epochs and other ---hyperparameters to potentially improve the model's performance.


Dataset Link - https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset


![Screenshot (21)](https://user-images.githubusercontent.com/108931665/202872673-baf566ad-7cb5-4471-a2f6-79db4716d958.png)

![Screenshot (14)](https://user-images.githubusercontent.com/108931665/202872675-c3a41028-b6e0-48f0-9d96-36770dd52201.png)

![Screenshot (18)](https://user-images.githubusercontent.com/108931665/202872676-88eadc66-073d-4f6b-ae75-a60f100db42c.png)
