![demo](/twitter-status/demo.png)

## Setting up
1. Install `selenium` and `scapy` python libraries. (or alternatively `python3-selenium` and `python3-scapy` packages)
2. Download the latest [geckodriver](https://github.com/mozilla/geckodriver/releases), rename the downlaoded file it to `geckodriver` and put it in `/usr/bin`
3. Find the interface you are going to monitor for twitter activity with `ifconfig` (or whatever you prefer)
4. put two images with `offline` and `online` in their name in `twitter-status` directory

## Using it
`sudo python3 main.py <interface name>@<non-root user>`

For example: `sudo python3 main.py wlp0s20f3@s0md3v`

When you run it for the first time, a browser window will open and it will ask you to login and once you do that, your cookies will be saved to a file named `cookies.json`.\
If you decide to change your twitter password, delete this file so it can be generated again with a fresh login.

> Note: root is required to monitor the interface but a non-root user is required to run selenium.

## FAQ
#### I am on windows, I don't have a `/usr/bin` direcotory.
Google 'install geckodriver windows', once you are done setting it up, update both geckodriver paths in `change.py`
#### I got an error or having a problem with this.
[Create an issue](https://github.com/s0md3v/dump/issues/new)
