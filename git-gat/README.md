Script to find (private) git repositories on *nix machines.

### Usage
`./git-gat`

The output should look like this:
```
/path/to/repo1/.git,http://example.com/user/repo1
/path/to/repo2/.git,git://example.com/user/repo2
/path/to/repo3/.git,git://example.com/user/repo3
```

#### Search custom directory
`./git-gat /home/user`

#### Include public repositories
`./git-gat /home/user all`
> Note: You can't use this option without specifying directory name.

### One liner
Three pre-built binaries are available: `linux_amd64`, `linux_arm64`, `macos_amd64`.\
To download+run one of them, you can do something like this:

```
wget https://github.com/s0md3v/dump/raw/master/git-gat/linux_amd64 -O /tmp/gat && ./tmp/gat
```
