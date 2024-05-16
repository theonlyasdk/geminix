from formatting import Format, format

def not_empty(str):
  """
  This function checks if a string is not empty.

  Args:
      str: The string to check.

  Returns:
      True if the string is not empty (after removing leading/trailing whitespaces), False otherwise.
  """
  return str.strip() != ""

def markdown_to_ansi(text: str) -> str:
  """
  Converts markdown formatting (bold) to ANSI escape sequences.

  Args:
      text (str): The markdown text to be converted.

  Returns:
      str: The text with converted markdown formatting.
  """

  formatted_text = ""
  start = 0
  while True:
    # Find the next occurrence of ** or its ending
    next_double_asterisk = text.find("**", start)
    next_double_asterisk_end = text.find("**", next_double_asterisk + 2) if next_double_asterisk != -1 else -1

    # Handle cases where no more bold formatting or unmatched closing ** is found
    if next_double_asterisk == -1:
      formatted_text += text[start:]
      break
    elif next_double_asterisk_end == -1:
      print("Warning: Unmatched closing '**' in markdown. Ignoring formatting.")
      formatted_text += text[start:next_double_asterisk + 2]
      start = next_double_asterisk + 2
      continue

    # Apply bold formatting to the text between ** markers
    formatted_text += text[start:next_double_asterisk]
    formatted_text += format(text[next_double_asterisk + 2:next_double_asterisk_end], Format.BOLD)
    start = next_double_asterisk_end + 2

  return formatted_text