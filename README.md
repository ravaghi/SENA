# SENA
This project focuses on document-level sentiment analysis of Norwegian news articles using a neural network architecture based on long-short-term-memory. Furthermore the hyperparameter optimization framework, [KerasTuner](https://keras.io/keras_tuner/), has been used to find the optimal hyperparameters for the network.

## Dataset
The dataset used in this project is the Norwegian Review Corpus, [NoReC](https://github.com/ltgoslo/norec), which has been made specifically for the purpose of training and evaluating models for document-level sentiment analysis. It is comprised of 43425 reviews collected from eight different sources in a number of different domains.

## Result
The model trained in the following figure managed to achieve an overall validation accuracy of 80%, but as the figure shows the model starts to overfit after 7 epochs. The reason for this was found to be the size of the dataset and its label imbalance.

![best_model_0 807860255241394-1](https://user-images.githubusercontent.com/44374191/165463393-a4b98de8-60fc-422b-b45f-6a957ab22a19.png)
