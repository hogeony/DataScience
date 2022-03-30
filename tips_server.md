### size for each folder
du -sh *

### check left size
df -Th

### copy folder/data form server A to server B
tar -cp <relative copy folder path in server A> | ssh <USERID@server B IP> -p <ssh port> tar xvp -C <aboslute destination path in server B>

ex) tar -cp test | ssh smile@123.123.123.123 -p 1234 tar xvp -C /data/test

### tar for compression
tar -cvf <filename.tar> <relative folder path to compress>

ex) tar -cvf test.tar test

### tar for extraction
tar -zcvf <filename.tar> <relative folder path to extract>

ex) tar -zcvf test.tar test

### Tar Usage and Options
c – create a archive file.
x – extract a archive file.
v – show the progress of archive file.
f – filename of archive file.
t – viewing content of archive file.
j – filter archive through bzip2.
z – filter archive through gzip.
r – append or update files or directories to existing archive file.

### manage permission
sudo chown <user>:<group> filename
sudo chown <user>:<group> *

### user
cat /etc/passwd
cut -f1 -d: /etc/passwd
grep /bin/bash /etc/passwd
grep /bin/bash /etc/passwd | cut -f1 -d:

sudo adduser <new user>
sudo usermod -aG sudo <new user>
sudo deluser <new user>

### miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda clean --all

### install liabraries for pytorch
conda install matplotlib seaborn opencv open3d scikit-learn pytorch torchvision torchaudio -c conda-forge -c open3d-admin

### kill process by grep
ps -ef | grep username | grep .py
kill -9 `ps -ef|grep username | grep .py|awk '{print $2}'`
