import re

def readfile(filename, string):
	return f"{string}\n{open(filename).read()}"

def extract_command(text: str) -> tuple[str, str, str] | None:
  """
  Extracts the command, filename, and message from a string in the format "<command> <filename>, <message>".

  Args:
      text (str): The input string.

  Returns:
      tuple[str, str, str] | None: A tuple containing the extracted command, filename, and message (or None if not found).
  """

  match = re.search(r"(?P<command>\w+)\s+(?P<filename>.+?)\, (?P<message>.+)", text)
  if match:
    return match.group("command"), match.group("filename"), match.group("message")
  else:
    return None