import argparse
import functools


def init_args(des: str, ops: dict):
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


def try_catch(err_handler):
  """Catch exceptions"""
  def wrapped(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        func(*args, **kwargs)
      except Exception as e:
        err_handler(e)
    return wrapper
  return wrapped
