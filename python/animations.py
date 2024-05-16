class LoadingAnimation:
  """
  A class for displaying a custom text loading animation in the background.
  """

  def __init__(self, text="Loading"):
    self.text = text
    self.animation = ["[■]", "[●]", "[○]", "[─]", "[·]"]
    self.index = 0
    self.running = False

  def set_text(self, text):
    self.text = text

  def start(self):
    self.running = True
    self.thread = threading.Thread(target=self._run_animation)
    self.thread.start()

  def stop(self):
    self.running = False
    print(" " * len(f"{self.text} {self.animation[self.index]}"), end="\r")

  def _run_animation(self):
    while self.running:
      print(f"{self.text} {self.animation[self.index]}", end="\r")
      self.index = (self.index + 1) % len(self.animation)
      time.sleep(0.1)
