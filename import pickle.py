import pickle

with open('configs\cifar100_l2p.py', 'rb') as f:
    try:
        ckpt_dict = pickle.load(f)
    except pickle.UnpicklingError as e:
        print(f"Error loading checkpoint: {e}")