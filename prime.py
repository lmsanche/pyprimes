import json
import argparse
import logging
import os
import datetime
import time

#****************************************
def config_log():
  #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  logging.root.handlers = []
  logging.basicConfig(level=logging.info,
  	                  format='%(asctime)s %(levelname)-8s %(message)s',
  	                  datefmt='%a, %d %b %Y %H:%M:%S',
  	                  filename='debug.log',
  	                  filemode='w')

  #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO, filename='ex.log')

  # set up logging to console
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  # set a format which is simpler for console use
  formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
  console.setFormatter(formatter)
  logging.getLogger("").addHandler(console)

  return True


#****************************************
def arguments():
  parser = argparse.ArgumentParser(description='Calculate prime numbers.')
  parser.add_argument('-f','--file', type=str, required=True, help='')
  parser.add_argument('-n','--number', required=True, type=int, help='')
  parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages to stderr')
  parser.add_argument('-i', '--info', action='store_true', default=False, help='print debug messages to stderr')
  args = parser.parse_args()

  if args.debug:
    logging.basicConfig(level=logging.DEBUG)

  if args.info:
    logging.basicConfig(level=logging.INFO)    

  fullpath = os.path.abspath(args.file)
  #print fullpath
  #os.path.exists(fullpath )  
  #os.stat(fullpath )


  #if args.file is not None:
  #		 parser.print_help()
  #		 exit

  return fullpath, args.number

#****************************************
def isprime(primes, value):
  for p in primes:
    if p != 1 and p != 0:
      if value % p == 0:
        return False
  return True


#****************************************
def load_values(file):
  primes = [0,1,2,3]

  if not os.path.exists(file):
    return primes

  else:
    with open(file, 'r') as infile:
      data = json.load(infile)
      primes = data['primes']

  return primes 

#****************************************
def store_values(file, primes):
  #data = primes
  data = {'primes': []}	
  data['primes'] = primes
  with open(file, 'w') as outfile:
    json.dump(data, outfile, sort_keys = True, indent = 4,
  ensure_ascii=False)
  return 

#****************************************
def generate(listprimes, value):
  for i in range(2,value):
    if i not in listprimes:
      if isprime(listprimes,i):
        listprimes.append (i)
        logging.info("End : " + str(time.ctime()))
  return listprimes

#****************************************
def main():
  # logging.info(main.__name__)
  logging.info("Begin : " + str(time.ctime()))
  start = time.time()
  #
  file, n = arguments()
  primes = load_values(file)
  primes = generate(primes, n)
  store_values (file, primes)

  # logging.info(primes)
  end = time.time()
  logging.info("End : " + str(time.ctime()))

  logging.info("Time : " + str(end - start))

if __name__ == "__main__":
  main()
