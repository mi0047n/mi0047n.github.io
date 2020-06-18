import os
import sys
import re
from os.path import dirname
cwd = dirname(os.getcwd())

directory = './index.md'


def check_if_string_in_file(file_name, string_to_search):
	return True


if check_if_string_in_file(directory, '##'):
   print('Yes')
else:
   print('No')
