Script to find (private) git repositories on linux machines.

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
