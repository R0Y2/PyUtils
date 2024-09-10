#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pyutils as pyu

_description = "PyUtils Test"
_options={
  'test_option':{
    'long': '--test_option',
    'short':'-t',
    'default': 'test.option'
  },
  'out_file':{
    'long':'--outfile',
    'short':'-o',
    'default': 'out.file'
  }
}

def assert_check(x):
  assert _description in repr(x)

@pyu.try_catch(assert_check)
@pyu.init_args(
  _description,
  _options
)
def main(parsed_args=None):
  if parsed_args.test_option == "exception":
    raise Exception(_description) 

if __name__ == '__main__':
  main()
