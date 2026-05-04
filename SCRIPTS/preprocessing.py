"""
This script should preprocess the image dataset before modeling.
Students are expected to complete the TODO sections inside each function.

Expected output:
    1. Resized images saved to DATA/processed/images/
    2. cleaned_metadata.csv
    3. train_metadata.csv
    4. test_metadata.csv

Run the project root:
    python SCRIPTS/preprocessing.py
"""


# ========================================
# Imports
# ========================================

from pathlib import Path
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split


# ========================================
# File path constants
# ========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "DATA"
RAW_IMAGE_DIR = DATA_DIR / "raw" / "images"
RAW_METADATA_PATH = DATA_DIR / "raw" / "metadata.csv"

PROCESSED_DIR = DATA_DIR / "processed"
PROCESSED_IMAGE_DIR = PROCESSED_DIR / "images"

CLEANED_METADATA_PATH = PROCESSED_DIR / "cleaned_metadata.csv"
TRAIN_METADATA_PATH = PROCESSED_DIR / "train_metadata.csv"
TEST_METADATA_PATH = PROCESSED_DIR / "test_metadata.csv"


# ========================================
# Preprocessing constants
# ========================================

IMAGE_SIZE = (224, 224)
TEST_SIZE = 0.20
RANDOM_STATE = 42

COLUMNS_TO_KEEP = [
    "image_name",
    "target",
    "age_approx",
    "sex",
    "anatom_site_general_challenge"
]

TARGET_COLUMN = "target"


# ========================================
# Helper functions
# ========================================

def create_directories():
    """
    Create the processed data directories if they do not already exist.

    GitHub does not track empty folders, so these folders may not exist
    when someone first clones the repository.

    1. Make PROCESSED_DIR.
    2. Make PROCESSED_IMAGE_DIR.
    """

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_IMAGE_DIR.mkdir(parents=True, exist_ok=True)


def load_metadata():
    """
    Load the metadata CSV file.

    1. Read the CSV file using pandas.
    2. Return the dataframe.
    """
    # TODO: Implement this function.
    pass


# ========================================
# Image preprocessing functions
# ========================================
def resize_images(metadata):
    """
    Resize all images listed in the metadata.

    1. Loop through each image name in the metadata.
    2. Resize and save each image. 
    """
    # TODO: Implement this function.
    pass


# ========================================
# Metadata preprocessing functions
# ========================================

def clean_metadata(metadata):
    """
    Remove unnecessary columns from the metadata.

    1. Keep only the columns needed for modeling and analysis.
    2. Save the cleaned metadata to CLEANED_METADATA_PATH.
    3. Return the cleaned metadata dataframe.
    """
    # TODO: Implement this function.
    pass


def split_train_test(metadata):
    """
    Split the metadata into training and test sets.

    1. Separate the metadata into train and test sets.
    2. Use stratified splitting based on TARGET_COLUMN.
    3. Use TEST_SIZE and RANDOM_STATE for reproducability.
    4. Save the training metadata to TRAIN_METADATA_PATH.
    5. SAVE the test metadata to TEST_METADATA_PATH.
    """
    # TODO: Implement this function
    pass


# ========================================
# Main
# ========================================

def main():
    """
    Run all preprocessing steps.
    """

    create_directories()

    metadata = load_metadata()
    cleaned_metadata = clean_metadata(metadata)

    resize_images(cleaned_metadata)
    split_train_test(cleaned_metadata)

    print("Preprocessing complete. Files saved in:", PROCESSED_DIR)


if __name__ == "__main__":
    main()
