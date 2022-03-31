### add, commit, push at once with commit msg: date
- git config --global alias.cmp '!f() { git add --all && git commit -m "`date`" && git push; }; f'
- git cmp

### add, commit, push at once with commit msg input
- git config --global alias.cmp '!f() { git add -A && git commit -m "$@" && git push; }; f'
- git cmp "msg"

### pull, add, commit, push at once with commit msg: date
- git config --global alias.pcmp '!f() { git pull && git add --all && git commit -m "`date`" && git push; }; f'
- git pcmp

### pull, add, commit, push at once with commit msg input
- git config --global alias.pcmp '!f() { git pull && git add -A && git commit -m "$@" && git push; }; f'
- git pcmp "msg"

### save credential information (id, password) for pulling, pushing
- git config credential.helper store

### ERROR => fatal: The remote end hung up unexpectedly
- git config --global http.postBuffer 104857600
- nano ~/.gitconfig

#### *it the error is not resolved, add the options below:*
- git config --global core.packedGitLimit 512m
- git config --global core.packedGitWindowSize 512m
- git config --global pack.deltaCacheSize 2047m
- git config --global pack.packSizeLimit 2047m
- git config --global pack.windowMemory 2047m

### credential (login via personal access token)
#### Set
- git config --global credential.helper store cache
#### Unset
- git config --unset credential.helper
    
### reset
- git log             <= show commits
- git reset HEAD      <= reset last commit
- git reset HEAD~10   <= reset previous 10 commits

### lfs
- sudo apt install curl
- sudo curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
- sudo apt-get install git-lfs
- git lfs install
- git rm -r --cached "*" <= if there is git add, unstaging
- git lfs track "filename"
