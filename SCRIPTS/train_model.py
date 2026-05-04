"""
This script should train the ResNet18 model on the processed image dataset.
Students are expected to complete the TODO sections inside each function.

Expected output:
    1. resnet18_model.pth
    2. training_accuracy.png

Run from the project root:
    python SCRIPTS/train_model.py
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
import torch.optim as optim

from torch.utils.data import DataLoader, TensorDataset
from torchvision import models, transforms


# ========================================
# File path constants
# ========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "DATA"
PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_IMAGE_DIR = PROCESSED_DIR / "images"

TRAIN_METADATA_PATH = PROCESSED_DIR / "train_metadata.csv"

OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
MODEL_DIR = OUTPUT_DIR / "model"
FIGURE_DIR = OUTPUT_DIR / "figures"

MODEL_PATH = MODEL_DIR / "resnet18_model.pth"
TRAINING_ACCURACY_PATH = FIGURE_DIR / "training_accuracy.png"


# ========================================
# Training constants
# ========================================

IMAGE_NAME_COLUMN = "image_name"
TARGET_COLUMN = "target"

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_EPOCHS = 10
LEARNING_RATE = 0.001
NUM_CLASSES = 2


# ========================================
# Helper functions
# ========================================

def create_directories():
    """
    Create the output directories if they do not already exist.

    GitHub does not track empty folders, so these folders may not exist
    when someone first clones the repository.

    1. Make MODEL_DIR.
    """

    MODEL_DIR.mkdir(parents=True, exist_ok=True)


# ========================================
# Data loading functions
# ========================================

def load_training_metadata():
    """
    Load the training metadata file.

    1. Read TRAIN_METADATA_PATH using pandas.
    2. Return the training dataframe.
    """
    # TODO: Implement this function.
    pass


def load_training_data(metadata):
    """
    Load the training images and labels.

    The metadata file tells us which images to load and what label each image has.
    This function opens each image, prepares it for ResNet18, stores its label, and
    returns a DataLoader that can be used during training.

    The DataLoader gives the model small batches of images instead of giving it the
    entire dataset all at once.

    1. Create image transformations.
    2. Loop through the training metadata.
    3. Open each image and store each image and label.
    4. Convert the image and label lists into tensors.
    5. Create and return a DataLoader.
    """
    
    # These transformations prepare images for ResNet18.
    # Resize makes every image 224 x 224.
    # ToTensor converts the image into numbers PyTorch can use.
    # Normalize uses the standard values expected by pretrained ResNet models.
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
    training_dataset = None

    # TODO: Create batches of data for training.
    # Hint: Use DataLoader() with BATCH_SIZE and shuffle=True.
    train_loader = None

    return train_loader


# ========================================
# Model functions
# ========================================

def build_model():
    """
    Build the ResNet18 model.

    ResNet18 is already trained to recognize general image patterns.
    We freeze the pretrained layers so they do not change during training.
    Then, we replace the final layer because our project only has two classes:
    benign and malignant. 

    1. Load a pretrained ResNet18 model.
    2. Freeze the pretrained layers.
    3. Replace the final layer so it predicts NUM_CLASSES classes.
    4. Return the model.
    """
    
    # TODO: Load a pretrained ResNet18 model.
    # Hint: Use models.resnet18() with pretrained weights.
    model = None

    # TODO: Freeze the pretrained layers.
    # Hint: Loop through model.parameters() and set requires_grad to False.
    for paremeter in None:
        paremeter.requires_grad = None

    # This gets the number of input features going into ResNet18's final layer.
    number_of_featurs = model.fc.in_features

    # TODO: Replace the final layer.
    # Hint: Use nn.Linear() with number_of_features and NUM_CLASSES.
    model.fc = None

    return model


def train_model(model, train_loader):
    """
    Train the model using the training data.

    The model looks at small batches of images, makes predictions, compares
    those predictions to the correct labels, and updates its final layer
    to improve over time.

    The function returns a list of training accuracy values, with one accuracy
    value for each epoch.

    1. Set up the loss function, optimizer, and accuracy list.
    2. Loop through the training data for NUM_EPOCHS.
    3. For each batch, make predictions and update the model based on the loss.
    4. Calculate and store the training accuracy for each epoch.
    5. Return the list of training accuracies.
    """
    
    # TODO: Create the loss function.
    # Hint: Use nn.CrossEntropyLoss()
    loss_function = None

    # TODO: Create the optimizer.
    # Hint: Use optim.Adam() with model.fc.parameters() and lr=LEARNING_RATE.
    optimizer = None

    training_accuracies = []

    for epoch in range(NUM_EPOCHS):

        # Put the model in training mode.
        model.train()

        number_correct = 0
        number_images = 0

        for images, labels in train_loader:

            # TODO: Use the model to make predictions for this batch.
            # Hint: Pass images into the model.
            predictions = None

            # TODO: Calculate the loss by comparing predictions and labels.
            # Hint: Use loss_function().
            loss = None

            # TODO: Clear the old gradients from the previous batch.
            # Hint: Use optimizer.zero_grad()

            # TODO: Backpropagate the loss.
            # Hint: Use loss.backward().

            # TODO: Update the model weights.
            # Hint: Use optimizer.step().

            # TODO: Find the class with the highest predicted score.
            # Hint: Use torch.argmax() with dim=1.

            # TODO: Count how many predictions were correct in this batch.
            number_correct += None

            # TODO: Count how many total images were in this batch.
            number_images += None

        # TODO: Calculate the training accuracy for this epoch.
        training_accuracy = None

        training_accuracies.append(training_accuracy)

        print(f"Epoch: {epoch + 1} Training Accuracy: {round(training_accuracy, 4)}")

    return training_accuracies


# ========================================
# Plotting functions
# ========================================

def plot_training_accuracy(training_accuracies):
    """
    Create a plot showing training accuracy over time.

    1. Plot training accuracy by epoch.
    2. Add a title.
    3. Add an x-axis label.
    4. Add a y-axis label.
    5. Save the figure to TRAINING_ACCURACY_PATH.
    """
    # TODO: Implement this function.
    pass


# ========================================
# Main
# ========================================

def main():
    """
    Run all model training steps.
    """

    create_directories()

    train_metadata = load_training_metadata()

    train_loader = load_training_data(train_metadata)

    model = build_model()

    training_accuracies = train_model(model, train_loader)

    torch.save(model.state_dict(), MODEL_PATH)

    plot_training_accuracy(training_accuracies)

    print("Training complete.")
    print("Model saved to:", MODEL_PATH)
    print("Training accuracy plot saved to:", TRAINING_ACCURACY_PATH)


if __name__ == "__main__":
    main()
