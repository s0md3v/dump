#!/usr/bin/env python2

import requests # Module for making HTTP requests
from requests.auth import HTTPBasicAuth # Importing a function which lets us submit HTTP auth credentials
import re # module for regular expression
import mechanize
import sys

br = mechanize.Browser() # Just shortening the calling function
br.set_handle_robots(False) # Don't follow robots.txt
br.set_handle_equiv(True) # I don't know what it does, but its some good shit
br.set_handle_redirect(True) # Follow redirects
br.set_handle_referer(True) # Include referrer
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
('Accept-Encoding', 'deflate'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

# Credentials for twilio.com API
account_sid = 'AC3d52962bb24fc862328655cc12d56cac'
auth_token = '7162aa51350db133549e62bf34adabae'

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

# Banner
print '''  %s.%s      _ .     . %s_%s_%s_%s
  | |%s\%s| /%s-%s | %s|%s\%s|%s |  |  %s`%s/
                       %s/%s
''' % (green, white, green, white, green, white, green, white, green, white, green, white, green, white, green, white, green, white,)

phone_number = raw_input('%s Enter the phone number: ' % que)
country_code = raw_input('%s Enter the country code: ' % que)
country_code = country_code.replace('+', '')
magic_sum = raw_input('%s Enter the magic sum: ' % que)

count = [] # a list for storing digits (only digits not x) contained in the entered number
possible = [] # all the possible combinations
validated = [] # the numbers from possible list validated by twilio.com API

# Function to extract digits from the entered number
def extract(phone_number):
    for x in list(phone_number):
        if x.isdigit(): # checks if x is a digit
            count.append(int(x))

# Function to set the limit for brutefocing
def limits(count):
    limit = []
    for x in range(phone_number.count('x')):
        limit.append('9')
    return int(''.join(limit))

# This function can find sum of digits contained in an integer
def get_sum(x):
   sum_of_x = 0
   while x:
       sum_of_x, x = sum_of_x + x % 10, x // 10
   return sum_of_x

# If we need to bruteforce for 3 digits and the magic sum should be 6, even 3 and 3 has a sum of 6 but we need
# 3 digits, so we will append a zero before it. This function appends a padding of zeros
def add_zero(length):
    padding = phone_number.count('x') - int(length)
    zero_dump = []
    for x in range(padding):
        zero_dump.append('0')
    return ''.join(zero_dump)

# Generates possible combinations
def bruteforce(phone_number):
    for x in range(0, limits(count)):
        new_number = phone_number
        if get_sum(x) == new_sum:
            if len(str(x)) != len(count):
                possible.append(re.sub(r'x+', add_zero(len(str(x))) + str(x), new_number))
            else:
                possible.append(re.sub(r'x+', str(x), new_number))

# Validates generated combinations with twilio.com API
def validate(database):
    for number in database:
        response = requests.get('https://lookups.twilio.com/v1/PhoneNumbers/%%2B%s%s' % (country_code, number) , auth=HTTPBasicAuth(account_sid, auth_token)).text
        if '"status": 404' not in response:
            validated.append(number)
    print '%s %i out of %i numbers are alive.' % (good, len(validated), len(possible))
    choice = raw_input('%s Would you like to store the numbers for further processing? [Y/n] ' % que).lower()
    if choice != 'n':
        save(possible)

# Uses facebook's password reset form to find user info
def get_info(database):
    for number in database:
        br.open('https://m.facebook.com/login/identify/?ctx=recover')
        br.select_form(nr=0)
        br.form['email'] = number
        req = br.submit()
        response = req.read()
        match = re.search(r'<div class="bi bj"><strong>[^<]*</strong></div>', response)
        if match:
            print '%s : %s' % (number, match.group().split('<div class="bi bj"><strong>')[1][:-15])

# A function to write stuff to a file
def save(list_to_save):
    with open ('%s.txt' % phone_number, 'a+') as text_file:
        for x in list_to_save:
            text_file.write(x + '\n')

extract(phone_number)
limits(count)

new_sum = int(magic_sum) - sum(count)

print '%s Generating all the possible combinations' % run
bruteforce(phone_number)
print '%s %i combination generated' % (good, len(possible))
choice = raw_input('%s Would you like to store the numbers for further processing? [Y/n] ' % que).lower()
if choice != 'n':
    save(possible)

choice = raw_input('%s Would you like to check which ones are alive? [Y/n] ' % que).lower()

if choice == 'n':
    print '%s Checking generated numbers for user info' % run
    get_info(possible)

else:
    validate(possible)
    print '%s Checking validated numbers for user info' % run
    get_info(validated)
