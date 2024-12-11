from py_utils.wrappers import try_catch, init_args

_description = "PyUtils Test"
_options={
  'test_option':{
    'long': '--test_option',
    'short':'-t',
    'default': 'test.exception' #'test.option'
  },
  'out_file':{
    'long':'--outfile',
    'short':'-o',
    'default': 'out.file'
  }
}

def assert_check(x):
  assert _description in repr(x)

def raise_except(e: Exception):
  raise(e)

#@try_catch(assert_check)
@try_catch(raise_except)
@init_args(
  _description,
  _options
)
def main(parsed_args=None):
  if parsed_args.test_option == "test.exception":
    raise Exception(_description) 

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    assert_check(e)
