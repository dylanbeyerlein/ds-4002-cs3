"""
This script should generate exploratory data analysis figures for the image dataset.
Students are expected to complete the TODO sections inside each function.

Expected output:
    1. class_distribution.png
    2. sample_images.png
    3. image_size_distribution.png
    4. age_distribution_by_class.png
    5. anatomical_site_by_class.png

Run from the project root:
    python SCRIPTS/eda.py
"""


# ========================================
# Imports
# ========================================

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


# ========================================
# File path constants
# ========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "DATA"
IMAGE_DIR = DATA_DIR / "raw" / "images"
METADATA_PATH = DATA_DIR / "raw" / "metadata.csv"

OUTPUT_DIR = PROJECT_ROOT / "OUTPUT" / "figures"
CLASS_DISTRIBUTION_PATH = OUTPUT_DIR / "class_distribution.png"
SAMPLE_IMAGES_PATH = OUTPUT_DIR / "sample_images.png"
IMAGE_SIZE_DISTRIBUTION_PATH = OUTPUT_DIR / "image_size_distribution.png"
AGE_DISTRIBUTION_PATH = OUTPUT_DIR / "age_distribution_by_class.png"
ANATOMICAL_SITE_PATH = OUTPUT_DIR / "anatomical_site_by_class.png"


# ========================================
# Helper functions
# ========================================

def load_metadata():
    """
    Load the metadata CSV file.

    1. Read the CSV file using pandas.
    2. Return the dataframe.
    """
    # TODO: Implement this function.
    pass


# ========================================
# Plotting functions
# ========================================

def plot_class_distributions(metadata):
    """
    Create a bar plot showing the number of benign and malignant images

    1. Count the number of images in each class.
    2. Create a bar plot.
    3. Add a title, x-axis label, and y-axis label.
    4. Save the figure to CLASS_DISTRIBUTION_PATH.
    """
    # TODO: Implement this function.
    pass


def plot_sample_images(metadata, num_images=5):
    """
    Create a grid of example benign and malignant images.

    1. Select num_images from each class.
    2. Load each image with PIL.Image.open().
    3. Display the images in a grid.
    4. Add a title and labels.
    5. Save the figure to SAMPLE_IMAGES_PATH.
    """
    # TODO: Implement this function.
    pass


def plot_image_size_distribution(metadata):
    """
    Create a plot showing the distribution of image sizes.

    1. Loop through the image files.
    2. Open each image with PIL.Image.open().
    3. Store the width and height of each iamge.
    4. Create a bar plot showing counts of each width x height pair.
    5. Save the figure to IMAGE_SIZE_DISTRIBUTION_PATH.
    """
    # TODO: Implement this function.
    pass


def plot_age_distribution_by_class(metadata):
    """
    Create a plot showing age distribution for benign and malignant images.

    1. Separate the metadata into benign and malignant groups.
    2. Create side by side histograms comparing age by class.
    3. Add a title, x-axis labels, y-axis labels, and legend.
    4. Save the figure to AGE_DISTRIBUTION_PATH.
    """
    # TODO: Implement this function.
    pass


def plot_anatomical_site_by_class(metadata):
    """
    Create a plot showing anatomical site counts by class.

    1. Count the number of images for each anatomical site within each class.
    2. Create side by side bar plots one for each class.
    3. Add a title, x-axis labels, y-axis labels, and legend.
    4. Save teh figure to ANATOMICAL_SITE_PATH.
    """
    # TODO: Implement this function
    pass


# ========================================
# Main
# ========================================

def main():
    """
    Run all EDA plotting functions.
    """

    metadata = load_metadata()

    plot_class_distributions(metadata)
    plot_sample_images(metadata, num_images=5)
    plot_image_size_distribution(metadata)
    plot_age_distribution_by_class(metadata)
    plot_anatomical_site_by_class(metadata)

    print("EDA complete. Figures saved in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
