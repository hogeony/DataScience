### size for each folder
- du -sh *

### check left size
- df -Th

### copy folder/data form server A to server B
- scp -r (relative copy folder path in server A) (USERID)@(server B IP):(aboslute destination path in server B)
- tar -cp (relative copy folder path in server A) | ssh (USERID@server B IP) -p (ssh port) tar xvp -C (aboslute destination path in server B)
- ex) tar -cp test | ssh smile@123.123.123.123 -p 1234 tar xvp -C /data/test

### tar for compression
- tar -cvf (filename.tar) (relative folder path to compress)
- ex) tar -cvf test.tar test

### tar for extraction
- tar -zcvf (filename.tar) (relative folder path to extract)
- ex) tar -zcvf test.tar test

### Tar Usage and Options
- c – create a archive file.
- x – extract a archive file.
- v – show the progress of archive file.
- f – filename of archive file.
- t – viewing content of archive file.
- j – filter archive through bzip2.
- z – filter archive through gzip.
- r – append or update files or directories to existing archive file.

### manage permission
- sudo chown (user):(group) filename
- sudo chown (user):(group) *

### user
- cat /etc/passwd
- cut -f1 -d: /etc/passwd
- grep /bin/bash /etc/passwd
- grep /bin/bash /etc/passwd | cut -f1 -d:
- sudo adduser (new user)
- sudo usermod -aG sudo (new user)
- sudo deluser (new user)

### reset user password
- /sbin/pam_tally2 --user (new user) --reset 

### miniconda
- wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
- source ~/.bashrc
- conda clean --all

### install liabraries for pytorch
- conda install matplotlib seaborn opencv open3d scikit-learn pytorch torchvision torchaudio -c conda-forge -c open3d-admin

### kill process by grep
- ps -ef | grep (username) | grep .py
- kill -9 \`ps -ef|grep (username) | grep .py|awk '{print $2}'\`

### basic installation
- wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
- bash Miniconda3-py39_4.11.0-Linux-x86_64.sh
- conda update conda
- conda install python
- conda update --all
- pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
- pip install tensorflow opencv-python open3d  python-telegram-bot scikit-learn pandas seaborn matplotlib

### check
```python
import torch
print(torch.cuda.is_available())

import tensorflow as tf
print(tf.config.experimental.list_logical_devices('GPU'))

import cv2, open3d
```
