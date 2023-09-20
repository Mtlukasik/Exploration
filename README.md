# Exploration



## Data Generation and Storage for Colab

This project facilitates the generation of synthetic data, specifically for creative packs and target store IDs. It also provides utilities for saving the data and associated metadata, ensuring traceability and reproducibility in Google Colab.
The project is structured with a configuration file (`data_generation_config.py`), utility functions (`data_generation_utils.py`), and a main Jupyter notebook to drive the data generation and storage process.

### Features:
1. Generate synthetic data based on specific configurations.
2. Save data in Parquet and TFRecord formats.
3. Save metadata containing real probabilities for creative packs and target store IDs.
4. Organized codebase for modularity and maintainability.
5. Data versioning to ensure traceability.

## Getting Started

### Prerequisites

- Google Colab environment.
- Google Drive integration for persistent storage.

### Instructions

1. **Mounting Google Drive**: Ensure you've integrated Google Drive with your Colab environment for saving datasets persistently.

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

2. **Setting up Configuration**: Edit `data_generation_config.py` to set your desired parameters:

   - `N_SAMPLES`, `N_TARGET_STORE_IDS`, and `N_CREATIVE_PACK_IDS` control the size and distribution of the generated data.
   - Paths for saving datasets, including versioning, are controlled with `DRIVE_PATH`, `PARQUET_FILENAME`, `TFRECORD_FILENAME`, and `METADATA_FILENAME`.

3. **Generating and Saving Data**: Run the main notebook. This notebook will utilize the utility functions to:

   - Generate synthetic data.
   - Save the dataset in both Parquet and TFRecord formats.
   - Save metadata (real probabilities) tied to the version of the dataset.

4. **Loading Data**: Utilize the provided functions in `data_generation_utils.py`:

   - `load_parquet()` to load the saved dataset in Parquet format.
   - `load_tfrecord()` to load the dataset in TFRecord format (if you implement this function).
   - `load_metadata()` to fetch the associated metadata for a specific dataset version.

## Contribute

Feedback and contributions to the project are welcome. Whether it's bug reports, new features, corrections, or any improvements, they can help the community.

