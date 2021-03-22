This is a hacky script that monitors your network activity for twitter usage and changes your twitter profile picture according to your online/offline status.

![demo](/twitter-status/demo.png)

## Setting up

> Note: If you are on windowss, scroll down to the FAQ section for general directions about how to get this working on windows.

1. Install `selenium` and `scapy` python libraries. (or alternatively `python3-selenium` and `python3-scapy` packages)
2. Download the latest [geckodriver](https://github.com/mozilla/geckodriver/releases), rename the downlaoded file to `geckodriver` and put it in `/usr/bin` directory
3. Find the network interface you are going to monitor for twitter activity with `ifconfig` (or whatever you prefer)
4. put two images with `offline` and `online` in their filename in the same directory as `main.py`

## Using it
`sudo python3 main.py <interface name>@<non-root user>`

For example: `sudo python3 main.py wlp0s20f3@s0md3v`

When you run it for the first time, a browser window will open and it will ask you to login and once you do that, your cookies will be saved to a file named `cookies.json`.\
Once this is done, you just need to run this script and it will do what its supposed to in the background.

## Useful information
1. root is required to monitor the interface but a non-root user is required because selenium can't be run as root.
2. If you stay inactive on twitter for 120 seconds, it will consider you offline. This threshold can be change by modifying the value of `inactivity_threshold` variable in `main.py`
3. You can run `python3 change.py online` and `python3 change.py offline` to change the profile picture manually.
4. If you decide to change your twitter password, delete the `cookies.json` file so it can be generated again with a fresh login.

## FAQ
#### I am on windows, how do I get this to run?
These are general directions, you will need to improvise as needed.

1. Search 'install geckodriver windows' on google, once you are done setting it up, update both geckodriver paths in `change.py`.
2. In linux, you do this to execute a command as another user: `sudo -u username <command>`. This might be different in Windows, find out how it should be and change the commands in `main.py` in `online()` function.

#### I got an error or having a problem with this.
[Create an issue](https://github.com/s0md3v/dump/issues/new)
