import os, h5py, time, numpy as np

root_npy = '/datasets/npy'
root_h5 = '/datasets/h5'
os.makedirs(root_h5, exist_ok=True)

def convert_npy_h5():
    file_list = os.listdir(root_npy)
    for filename in file_list:

        file_load_path = os.path.join(root_npy, filename)
        data = np.load(file_path)

        file_save_path = os.path.join(root_h5, filename.replace('npy', 'h5'))
        with h5py.File(file_save_path, 'w') as f:
            f.create_dataset('data', data=data)

        print(file_save_path)

convert_npy_h5()

t_start = time.time()
file_list = os.listdir(root_npy)
for filename in file_list:
    file_load_path = os.path.join(root_npy, filename)
    data = np.load(file_path)
print(time.time()-t_start)

t_start = time.time()
file_list = os.listdir(root_h5)
for filename in file_list:
    file_load_path = os.path.join(root_h5, filename)
    with h5py.File(file_load_path, 'w') as f:
        data=f.get('data')
print(time.time()-t_start)
