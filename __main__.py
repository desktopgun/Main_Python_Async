
import os
import sys
import asyncio
import inspect
import importlib
from typing import Any, Awaitable

args = sys.argv
cmd_path = f"{os.path.abspath( os.path.dirname( __file__ ) )}"

async def run_sequence(*functions: Awaitable[Any]) -> None:
  for function in functions: await function

async def run_parallel(*functions: Awaitable[Any]) -> None:
  await asyncio.gather(*functions)

async def check_args():

  if len(args) >= 1:      
    arg = args[1]
    dir_path = f"{cmd_path}/{'/'.join(arg.split('.'))}"
    if len(arg.split('.')) >= 2:
      if os.path.isdir(dir_path):
        module = importlib.import_module(arg)
      elif os.path.isfile(f"{dir_path}.py"):
        module = importlib.import_module(arg)
      else:pass#print('neither file or directory')
    elif len(arg.split('.')) == 1:
      if os.path.isdir(dir_path):
        module = importlib.import_module(arg)
      elif os.path.isfile(f"{dir_path}.py"):
        module = importlib.import_module(arg)
      else:pass#print('neither file or directory')

  if len(args) >= 2:

    for arg in args[2:]:

      if len(arg.split('.')) == 2:
        try:
          theclass = getattr(module, arg.split('.')[0])
          class_full_args = inspect.getfullargspec(theclass)
          theclass()
          themethod = getattr(theclass, arg.split('.')[1])
          method_full_args = inspect.getfullargspec(themethod) 
          params = args[3:]
          if 'self' in method_full_args[0]:
            params.insert(0, '()')
            if args[3:]:await themethod(*params)
            elif not args[3:]:await themethod(*params)

          else:
            if args[3:]:
              if method_full_args[1] != None:await themethod(*params)
              elif method_full_args[1] == None:await themethod()
            elif not args[3:]:await themethod()

        #except Exception as err:
        #  print('error 2',err)
        except:pass

      elif len(arg.split('.')) == 1:

        try:
          themethod = getattr(module, arg)
          method_full_args = inspect.getfullargspec(themethod) 
          params = args[3:]

          if 'self' in method_full_args[0]:
            params.insert(0, '()')
            if args[3:]:await themethod(*params)
            elif not args[3:]:await themethod(*params)

          else:
            if args[3:]:
              if method_full_args[1] != None:await themethod(*params)
              elif method_full_args[1] == None:await themethod()
            elif not args[3:]:await themethod()

        #except Exception as err:
        #  print('error 2',err)
        except:pass

async def startup():
  await run_parallel(
    #add another func here, 
    check_args(),
  )

if __name__ == '__main__':
  try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([
      #add another func here 
      startup()
    ]))
  except KeyboardInterrupt:quit()
  except Exception as err:print('****ERROR****',err)
