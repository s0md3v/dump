import json
import re
import sys

burp_regex = r'''<mimetype>JSON</mimetype>[\s\n]+<response base64="false"><!\[CDATA\[HTTP/[\d.]+ \d{3} [^\n]+\n(?:[A-Za-z-]+: .+?\n)+\n([\s\S]+?)\]\]></response>'''
key_regex = r'[^\\]"([^"]+[^\\])":'

output = set()

def prefix_path(arg):
    if '+' not in arg:
        return '', arg
    return arg.split('+')[0], arg.split('+')[-1]

def argparse():
    if len(sys.argv) == 2:
        prefix, path = prefix_path(sys.argv[1])
        return {"modes": ["p"], "path": path, "prefix": prefix}
    elif len(sys.argv) > 2:
        prefix, path = prefix_path(sys.argv[2])
        if sys.argv[1].startswith('-'):
            for option in list(sys.argv[1].lstrip('-')):
                if option not in ('p', 'k'):
                    return f"invalid option {option}"
            return {"modes": list(sys.argv[1].lstrip('-')), "path": path, "prefix": prefix}
        return {"modes": ["p"], "path": path, "prefix": prefix}
    return "invalid number of options"

def convert_json(val, old=""):
    if isinstance(val, dict):
        for k in val.keys():
            convert_json(val[k], old + "/" + str(k))
    elif isinstance(val, list):
        for i,k in enumerate(val):
            convert_json(k, old + "/" + str(i))
    if old:
        output.add(old.lstrip('/'))

def get_keys(string):
    return re.findall(key_regex, string)

def parse_burp_export(path, modes):
    """
    extracts JSON responses from burp suite
    and parses them to extract json keys
    returns set (of request objects)
    """
    global output
    burp_file = open(path, 'r')
    content = burp_file.read()
    burp_file.close()
    matches = re.findall(burp_regex, content)
    for match in matches:
        if 'k' in modes:
            output = output.union(get_keys(match))
        if 'p' in modes:
            convert_json(json.loads(match))

def main():
    args = argparse()
    if type(args) == str:
        print("Error:", args, file=sys.stderr, end="\n\n")
        print('''Usage: j2p <options> <prefix>+<path to burp-file>
            \nAvailable options:
    p: print paths
    k: print keys
            \n<prefix>+ and <options> are optional.
            \nExamples:
    > j2p -p test.txt
    > j2p -pk /+test.txt''',
            file=sys.stderr)
        exit(1)
    path, modes, prefix = args['path'], args['modes'], args['prefix']
    parse_burp_export(path, modes)
    for path in output:
        print(prefix + path)
