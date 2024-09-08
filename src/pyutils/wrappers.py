#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import functools
import traceback


def init_args(des: "description", ops: "options dict"):
  """Init commandline arguments"""
  def wrapped(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      parser = argparse.ArgumentParser(
        description=des,
        formatter_class=argparse.RawTextHelpFormatter
      )
      for opk,opv in ops.items():
        parser.add_argument(
          opv['long'],
          opv['short'],
          metavar=opk,
          default=opv['default'],
          help="(default: %(default)s)"
        )
      rtn = func(parser.parse_args(), *args, **kwargs,)
      return rtn
    return wrapper
  return wrapped


def try_catch(call_back):
  """Catch exceptions"""
  def wrapped(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        func(*args, **kwargs)
      except Exception as e:
        call_back(repr(e))
        call_back(traceback.format_exc())
    return wrapper
  return wrapped
