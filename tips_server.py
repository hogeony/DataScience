# copy folder/data form server A to server B

# bash / terminal
tar -cp <relative copy folder path in server A> | ssh <USERID@server B IP> -p <ssh port> tar xvp -C <aboslute destination path in server B>
ex) tar -cp test | ssh smile@123.123.123.123 -p 1234 tar xvp -C /data/test

# tar for compression
tar -cvf <filename.tar> <relative folder path to compress>
ex) tar -cvf test.tar test

# tar for extraction
tar -zcvf <filename.tar> <relative folder path to extract>
ex) tar -zcvf test.tar test

# Tar Usage and Options
c – create a archive file.
x – extract a archive file.
v – show the progress of archive file.
f – filename of archive file.
t – viewing content of archive file.
j – filter archive through bzip2.
z – filter archive through gzip.
r – append or update files or directories to existing archive file.

# manage permission
sudo chown <user>:<group> filename
sudo chown <user>:<group> *

# add, commit, push at once with commit msg: date
git config --global alias.cmp '!f() { git add --all && git commit -m "`date`" && git push; }; f'
git cmp

# add, commit, push at once with commit msg input
git config --global alias.cmp '!f() { git add -A && git commit -m "$@" && git push; }; f'
git cmp "msg"

# pull, add, commit, push at once with commit msg: date
git config --global alias.pcmp '!f() { git pull && git add --all && git commit -m "`date`" && git push; }; f'
git pcmp

# pull, add, commit, push at once with commit msg input
git config --global alias.pcmp '!f() { git pull && git add -A && git commit -m "$@" && git push; }; f'
git pcmp "msg"
