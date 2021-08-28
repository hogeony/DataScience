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

# save credential information (id, password) for pulling, pushing
git config credential.helper store

# ERROR => fatal: The remote end hung up unexpectedly
git config --global http.postBuffer 104857600
nano ~/.gitconfig
--- it the error is not resolved, add the options below:
git config --global core.packedGitLimit 512m
git config --global core.packedGitWindowSize 512m
git config --global pack.deltaCacheSize 2047m
git config --global pack.packSizeLimit 2047m
git config --global pack.windowMemory 2047m
