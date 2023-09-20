# Exploration
Features:
Generate synthetic data based on specific configurations.
Save data in Parquet and TFRecord formats.
Save metadata containing real probabilities for creative packs and target store IDs.
Organized codebase for modularity and maintainability.
Data versioning to ensure traceability.
Getting Started
Prerequisites
Google Colab environment.
Google Drive integration for persistent storage.
Instructions
Mounting Google Drive: Ensure you've integrated Google Drive with your Colab environment for saving datasets persistently.

python
Copy code
from google.colab import drive
drive.mount('/content/drive')
Setting up Configuration: Edit data_generation_config.py to set your desired parameters:

N_SAMPLES, N_TARGET_STORE_IDS, and N_CREATIVE_PACK_IDS control the size and distribution of the generated data.
Paths for saving datasets, including versioning, are controlled with DRIVE_PATH, PARQUET_FILENAME, TFRECORD_FILENAME, and METADATA_FILENAME.
Generating and Saving Data: Run the main notebook. This notebook will utilize the utility functions to:

Generate synthetic data.
Save the dataset in both Parquet and TFRecord formats.
Save metadata (real probabilities) tied to the version of the dataset.
Loading Data: Utilize the provided functions in data_generation_utils.py:

load_parquet() to load the saved dataset in Parquet format.
load_tfrecord() to load the dataset in TFRecord format (if you implement this function).
load_metadata() to fetch the associated metadata for a specific dataset version.
Contribute
Feedback and contributions to the project are welcome. Whether it's bug reports, new features, corrections, or any improvements, they can help the community.

This README provides a concise overview of the project. Depending on the audience and the depth of detail you want to go into, you might also want to consider adding sections on the actual algorithm used for data generation, performance benchmarks (if any), and more detailed instructions for contributions.
