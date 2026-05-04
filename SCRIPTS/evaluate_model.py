"""
Evaluate the trained ResNet18 model on the processed test dataset.
Students are expected to complete the TODO sections inside each function.

Expected output:
    1. metrics.csv
    2. confusion_matrix.png
    3. roc_curve.png

Run from the project root:
    python SCRIPTS/evaluate_model.py
"""


# ========================================
# Imports
# ========================================

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset
from torchvision import models, transforms

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay


# ========================================
# File path constants
# ========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "DATA"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_IMAGE_DIR = PROCESSED_DIR / "images"

TEST_METADATA_PATH = PROCESSED_DIR / "test_metadata.csv"

OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
MODEL_DIR = OUTPUT_DIR / "model"
FIGURE_DIR = OUTPUT_DIR / "figures"

MODEL_PATH = MODEL_DIR / "resnet18_model.pth"
METRICS_PATH = OUTPUT_DIR / "metrics.csv"
CONFUSION_MATRIX_PATH = FIGURE_DIR / "confusion_matrix.png"
ROC_CURVE_PATH = FIGURE_DIR / "roc_curve.png"


# ========================================
# Evaluation constants
# ========================================

IMAGE_NAME_COLUMN = "image_name"
TARGET_COLUMN = "target"

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 2

CLASS_NAMES = ["benign", "malignant"]


# ========================================
# Data loading functions
# ========================================

def load_test_metadata():
    """
    Load the test metadata file.

    1. Read TEST_METADATA_PATH using pandas.
    2. Return the test dataframe.
    """
    # TODO: Implement this function.
    pass


def load_test_data(metadata):
    """
    Load the test images and labels.

    The metadata file tells us which images to load and what label each image has.
    This function opens each image, prepares it for ResNet18, stores its label, and
    returns a DataLoader that can be used during evaluation.

    The DataLoader gives the model small batches of images instead of giving it the
    entire dataset all at once.

    1. Create image transformations.
    2. Loop through the test metadata.
    3. Open each image and store each image and label.
    4. Convert the image and label lists into tensors.
    5. Create and return a DataLoader.
    """
    
    # These transformations should match the transformations used during training.
    image_transform = transforms.Compose([
        transforms.Resize(IMAGE_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    images = []
    labels = []

    for index, row in metadata.iterrows():
        # TODO: Get the image name from the metadata row.
        # Hint: Use IMAGE_NAME_COLUMN.
        image_name = None

        # TODO: Create the full image path.
        # Hint: Add ".jpg" to the image name and use PROCESSED_IMAGE_DIR.
        image_path = None

        # TODO: Open the image and convert it to RGB format.
        # Hint: Use Image.open() and .convert("RGB").
        image = None

        # TODO: Apply the image transformations.
        # Hint: Use image_transform().
        image = None

        # TODO: Get the label from the metadata row.
        # Hint: Use TARGET_COLUMN.
        label = None

        images.append(image)
        labels.append(label)

    # TODO: Combine the list of image tensors into one large tensor.
    # Hint: Use torch.stack().
    image_tensor = None

    # TODO: Convert the labels list into a tensor.
    # Hint: Use torch.tensor().
    label_tensor = None

    # TODO: Store the images and labels together.
    # Hint: Use TensorDataset().
    test_dataset = None

    # TODO: Create batches of test data.
    # Hint: Use DataLoader() with BATCH_SIZE and shuffle=False.
    test_loader = None

    return test_loader


def build_model():
    """
    Build the ResNet18 model.

    ResNet18 is already trained to recognize general image patterns.
    Then, we replace the final layer because our project only has two classes:
    benign and malignant. 

    This must match the model architecture used during training.

    1. Create a ResNet18 model structure.
    2. Replace the final layer so it predicts NUM_CLASSES classes.
    3. Return the model.
    """
    
    # TODO: Create a ResNet18 model structure.
    # Hint: Use weights=None because we are loading our saved trained weights.
    model = None

    # This gets the number of input features going into ResNet18's final layer.
    number_of_features = model.fc.in_features

    # TODO: Replace the final layer.
    # Hint: Use nn.Linear() with number_of_features and NUM_CLASSES.
    model.fc = None

    return model


def load_trained_model():
    """
    Load the saved model weights.

    The training script saved the model weights to MODEL_PATH.
    This function rebuilds the same model structure and loads those weights.

    1. Rebuild the same model strucutre used during training.
    2. Load the saved model weights from MODEL_PATH.
    3. Add the saved weights to the model and return it.
    """

    model = build_model()

    # TODO: Load the saved model weights and add them to the model.
    # Hint: Use torch.load() and model.load_state_dict().

    return model


# ========================================
# Prediction functions
# ========================================

def make_predictions(model, test_loader):
    """
    Use the trained model to make predictions on the test data.

    The model has already been trained, so this function does not update the model
    weights. Instead, it sends the test images through the model and records what 
    the model predicted.

    For each test image, the model gives output scores for both classes:
        0 = benign
        1 = malignant
    
    We convert those scores into probabilities and choose the class with the highest
    score as the model's predicted label.

    1. Put the model in evaluation mode.
    2. Create empty lists for true labels, predicted labels, and predicted probabilities.
    3. Loop through the test batches.
    4. Use the model to generate output scores and convert them into probabilities.
    5. Get the predicted class for each image.
    6. Store and return the true labels, predicted labels, and malignant-class probabilities.
    """

    model.eval()

    true_labels = []
    predicted_labels = []
    predicted_probabilities = []

    # torch.no_grad() tells PyTorch that we are not training.
    with torch.no_grad():

        for images, labels in test_loader:

            # TODO: Use the model to make predictions.
            predictions = None

            # TODO: Convert prediction scores into probabilities.
            # Hint: Use torch.softmax() with dim=1.
            probabilities = None

            # TODO: Find the predicted class with the highest score.
            # Hint: Use torch.argmax() with dim=1.
            classes = None

            # Store the true labels.
            true_labels.extend(labels.tolist())

            # Store the predicted labels.
            predicted_labels.extend(classes.tolist())

            # Store the probability of class 1.
            # Class 1 is the malignant class.
            predicted_probabilities.extend(probabilities[:, 1].tolist())

    return true_labels, predicted_labels, predicted_probabilities


# ========================================
# Metric functions
# ========================================

def calculate_metrics(true_labels, predicted_labels, predicted_probabilities):
    """
    Calculate evaluation metrics and save them to METRICS_PATH.

    1. Calculate accuracy.
    2. Calculate precision.
    3. Calculate recall.
    4. Calculate F1 score.
    5. Calculate ROC-AUC.
    6. Store the metrics in a dataframe and save it to METRICS_PATH.
    """
    # TODO: Implement this function.
    pass


# ========================================
# Plotting functions
# ========================================

def plot_confusion_matrix(true_labels, predicted_labels):
    """
    Create and save a confusion matrix plot.

    1. Calculate the confusion matrix.
    2. Display the confusion matrix with class labels.
    3. Add a title.
    4. Save the figure to CONFUSION_MATRIX_PATH.
    """
    # TODO: Implement this function.
    pass


def plot_roc_curve(true_labels, predicted_probabilities):
    """
    Create and save an ROC curve plot.

    1. Calculate the false positive rate and true positive rate.
    2. Create the ROC curve plot.
    3. Add a title.
    4. Save the figure to ROC_CURVE_PATH.
    """
    # TODO: Implement this function.
    pass


# ========================================
# Main
# ========================================

def main():
    """
    Run all model evaluation steps.
    """

    test_metadata = load_test_metadata()

    test_loader = load_test_data(test_metadata)

    model = load_trained_model()

    true_labels, predicted_labels, predicted_probabilities = make_predictions(
        model,
        test_loader
    )

    calculate_metrics(
        true_labels,
        predicted_labels,
        predicted_probabilities
    )

    plot_confusion_matrix(true_labels, predicted_labels)

    plot_roc_curve(true_labels, predicted_probabilities)

    print("Evaluation complete.")
    print("Metrics saved to:", METRICS_PATH)
    print("Confusion matrix saved to:", CONFUSION_MATRIX_PATH)
    print("ROC curve saved to:", ROC_CURVE_PATH)


if __name__ == "__main__":
    main()
