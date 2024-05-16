from formatting import Format, format

def error(msg):
  print(f"{format('Oops!', Format.YELLOW)} {msg}")
  exit(-1)
