import pandas as pd
import numpy as np
import os

print("Loading test_dataset.csv...")
df = pd.read_csv('dataset_rishiraj/test_set/test_dataset.csv')

print("Mapping countries...")
def get_country(row):
    if row.get('country_France', False): return 'France'
    if row.get('country_India', False): return 'India'
    if row.get('country_US', False): return 'US'
    return ''

df['country'] = df.apply(get_country, axis=1)

os.makedirs('dataset/test', exist_ok=True)
os.makedirs('dataset/train', exist_ok=True)

# Also copy train source files if needed by run_pipeline_v2.py, but it uses cleaned_dataset/training_data.csv directly.
# Wait, setup_colab.sh linked student_resource/dataset to dataset.
# The pipeline just reads dataset/test/test_source*.tsv.

for s in ['S1', 'S2', 'S3']:
    print(f"Filtering {s}...")
    mask = df['entity_id'].str.startswith(f"{s}-")
    sub_df = df[mask]
    
    out_path = f"dataset/test/test_source{s[-1]}.tsv"
    sub_df[['entity_id', 'country', 'business_name', 'business_address']].to_csv(out_path, sep='\t', index=False)
    print(f"Saved {len(sub_df)} rows to {out_path}")

print("Done.")
