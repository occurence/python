import time

@contextlib.contextmanager
def timer():
  """Time how long code in the context block takes to run."""
  t0 = time.time()
  try:
      yield
  except:
    raise
  finally:
    t1 = time.time()
    print('Elapsed: {:.2f} seconds'.format(t1 - t0))

def process_with_numpy(p):
  _process_pic(0.1521)

def process_with_pytorch(p):
  _process_pic(0.0328)


image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)