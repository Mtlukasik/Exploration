import numpy as np
import pandas as pd
import string, random
import tensorflow as tf
from google.colab import drive
import data_generation_config as config
import json

# Importing constants from data_generation_config
n_samples = config.N_SAMPLES
n_target_store_ids = config.N_TARGET_STORE_IDS
n_creative_pack_ids = config.N_CREATIVE_PACK_IDS

# Data Generation Functions
def lower_string(length, string1=''): 
    result = string1+''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result
    
def generate_data():
    global n_target_store_ids, n_creative_pack_ids, n_samples
    target_store_ids = {i:lower_string(10,'target_') for i in (range(0, n_target_store_ids))}
    creative_pack_ids = {i:lower_string(10,'creative_') for i in (range(0, n_creative_pack_ids))}
    
    output = [i for i in range(0, n_target_store_ids)]
    target_store_id_probs = {i:j for i,j in enumerate(np.linspace(0, 1, n_target_store_ids+2)[1:-1])}
    creative_pack_id_probs = {i:j for i,j in enumerate(np.random.uniform(-0.01, 0.01, n_creative_pack_ids))}
    
    def assign_probability(idc):
        choice = random.choice(output)
        if (target_store_id_probs[choice] + creative_pack_id_probs[idc] >1) or (target_store_id_probs[choice] + creative_pack_id_probs[idc] <0):
          return {(idc,choice) : target_store_id_probs[choice] - creative_pack_id_probs[idc]}
        else:
          return {(idc,choice) : target_store_id_probs[choice] + creative_pack_id_probs[idc]}
    
    creative_mapping2target = [assign_probability(idc) for idc,string in enumerate(creative_pack_ids)]
    
    dataset_cp = []
    dataset_tg = []
    dataset_label = []
    
    def generate_sample(creative_mapping2target):
      case_chosen = random.choice(creative_mapping2target)
      cp_tg_chosen = list(case_chosen.keys())[0]
      probability = case_chosen[cp_tg_chosen]
      dataset_cp.append(creative_pack_ids[cp_tg_chosen[0]]),dataset_tg.append(target_store_ids[cp_tg_chosen[1]]),dataset_label.append(np.random.binomial(1, probability))
    
    [generate_sample(creative_mapping2target) for i in range(n_samples)]
    
    dataset = pd.DataFrame({"target_store_id": dataset_tg,
                            "creative_pack_id": dataset_cp,
                            "label": dataset_label})

    return dataset

# Saving Functions
def save_as_parquet(dataset):
    save_path_parquet = config.DRIVE_PATH + config.PARQUET_FILENAME.format(config.VERSION)
    dataset.to_parquet(save_path_parquet, index=False)

def save_as_tfrecord(dataset):
    # ... [Your TFRecord saving code here]
    tfrecord_path = config.DRIVE_PATH + config.TFRECORD_FILENAME.format(config.VERSION)
    with tf.io.TFRecordWriter(tfrecord_path) as writer:
        for _, row in dataset.iterrows():
            example = serialize_example(row["target_store_id"], row["creative_pack_id"], row["label"])
            writer.write(example)

# Loading Functions (You can extend these as per your requirements)
def load_parquet():
    load_path_parquet = config.DRIVE_PATH + config.PARQUET_FILENAME.format(config.VERSION)
    return pd.read_parquet(load_path_parquet)

def load_tfrecord():
    feature_description = {
        'target_store_id': tf.io.FixedLenFeature([], tf.string),
        'creative_pack_id': tf.io.FixedLenFeature([], tf.string),
        'label': tf.io.FixedLenFeature([], tf.int64)
    }
    
    def _parse_function(example_proto):
        return tf.io.parse_single_example(example_proto, feature_description)
    
    # Load dataset from TFRecord
    tfrecord_dataset = tf.data.TFRecordDataset("/content/drive/My Drive/dataset_v1.tfrecord")
    parsed_dataset = tfrecord_dataset.map(_parse_function)
    return parsed_dataset


# Saving Functions
def save_metadata(creative_pack_id_probs, target_store_id_probs):
    metadata = {
        'creative_pack_id_probs': creative_pack_id_probs,
        'target_store_id_probs': target_store_id_probs
    }
    metadata_path = config.DRIVE_PATH + config.METADATA_FILENAME.format(config.VERSION)
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f)

# Loading Functions
def load_metadata():
    metadata_path = config.DRIVE_PATH + config.METADATA_FILENAME.format(config.VERSION)
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    return metadata
