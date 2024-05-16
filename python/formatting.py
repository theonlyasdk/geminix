class Format:
  """
  This class provides color codes and formatting options for text in the terminal.

  These codes can be used to enhance the readability and visual appeal of text output 
  in terminal applications. However, it's important to note that some terminals may 
  not support all formatting options (like italics).
  """

  RED = "\033[31m"  # Red color
  GREEN = "\033[32m"  # Green color
  YELLOW = "\033[33m"  # Yellow color
  BLUE = "\033[34m"  # Blue color
  MAGENTA = "\033[35m"  # Magenta color
  CYAN = "\033[36m"  # Cyan color
  RESET = "\033[0m"  # Reset formatting to default
  BOLD = "\033[1m"  # Bold text
  ITALIC = "\033[3m"  # Italic text (may not be supported by all terminals)
  UNDERLINE = "\033[4m"  # Underline text

def format(text, fmt):
  """
  This method formats a string with the specified format code.

  Args:
    text: The text to be formatted.
    fmt: The format code to apply (e.g., Format.RED, Format.BOLD).

  Returns:
    The formatted string.
  """
  return fmt + text + Format.RESET