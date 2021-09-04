This tool finds hidden endpoints, especially on APIs.
It fetches JSON responses from BurpSuite history and creates url-paths wordlist from JSON keys.

![j2p-demo](https://i.ibb.co/YTZLVrz/demo.png)

### Installation
```
pip3 install json2paths
```

### How to export BurpSuite history?
Select all responses you want to export, right click the selection and choose "save items" from the menu. Make sure base64 encoding is turned off in saving dialogue.

### Usage
For more information about how to use this tool, fuck around and find out.
```
Usage: j2p <options> <prefix>+<path to burp-file>

Available options:
    p: print paths
    k: print keys

<prefix>+ and <options> are optional.

Examples:
    > j2p -p test.txt
    > j2p -pk /+test.txt
```
