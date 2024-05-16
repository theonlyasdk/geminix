"""
Python TTY frontend for Geminix
(c) theonlyasdk 2024
"""

import google.generativeai as genai
import json
import commands
import os
import datetime

from formatting import Format, format
from animations import LoadingAnimation
from strings import not_empty, markdown_to_ansi
from logger import error

if not os.path.isfile(os.path.expanduser("config/config.json")):
  error("This is fatal. Where is my config file? You'll have to get my config.json back.")

config = json.load(open("config/config.json"))

def load_config_from_json(key):
  return json.load(open("config/" + config['config_files'][key]))

api_key_path = config['config_files']["api_key"]

if os.path.isfile(os.path.expanduser(api_key_path)):
  with open(api_key_path, "r") as f:
    content = f.read().strip()
    if not content:
      error("The token file is empty! Please refer to README.md for instructions on how to obtain your Gemini API key")
else:
  error("Token file is missing! Please create a 'token.secret' file in the 'env' directory and paste your Gemini API key in it!")

api_key = open(api_key_path).read().replace('\n', '')
safety_settings = load_config_from_json("safety_settings")
initial_conversation = load_config_from_json("initial_conversation")
generation_config = load_config_from_json("generation_config")
app_running = True

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=initial_conversation)
animation_thinking = LoadingAnimation("Thinking...")

def send_message(msg):
    animation_thinking.start()
    convo.send_message(msg)
    animation_thinking.stop()

def send_message_and_get_reply(msg):
    send_message(msg)
    print(markdown_to_ansi(convo.last.text))

def exit_app():
    print(config['events']['on_app_exit']['tell_user'])
    exit(0)

print(format(config['events']['on_app_open']['tell_user'], Format.BOLD))
send_message_and_get_reply(config['events']['on_app_open']['tell_model'])

while app_running:
  prompt = input(format("> ", Format.BOLD))
  
  if not_empty(prompt):
    if convo.last.text.__contains__("GEMINIX_EXIT") or prompt == "exit":
      exit_app()

    if commands.extract_command(prompt) is not None:
      command, filename, message = commands.extract_command(prompt)
      
      if command == "read":
        send_message_and_get_reply(commands.readfile(filename.strip(), message.strip()))
      if command == "save":
        os.makedirs("saved_responses", exist_ok=True)

        date_today = datetime.date.today().strftime('%Y-%m-%d')
        save_to_filename = "saved_responses/{filename}_{date_today}.txt"
        print(f"Saving last response into 'saved_responses/{save_to_filename}'...")

        file = open(save_to_filename, "w")
        file.write(convo.last.text)
        file.close()
    else:
      send_message_and_get_reply(prompt)