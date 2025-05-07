# scripts/convert_yaml_to_pkl.py

import yaml
import pickle

def convert_yaml_to_pkl(yaml_file, pkl_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    
    with open(pkl_file, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)

convert_yaml_to_pkl('configs/topo.yaml', 'configs/topo.pkl')
