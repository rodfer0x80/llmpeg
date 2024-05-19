import nltk

class Triggers:
  audio_check = ["from", "by", "song", "music", "play"]
  audio_start = "play"
  goodbye = ["bye", "goodbye"]
  greeting = ["hi", "hello", "hey", "greetings"]
  goodbye_default_phrase = ["see", "you", "next", "time"]
  browse_check = ["search", "browse", "find", "lookup", "read about", "look up", "research",
                  "explore", "investigate", "investigation", "study", "examine", "inspect", "scrutinize", "analyze"]
  browse_start = "browse"
  explain_check = ["explain", "and", "it", "the", "results",
                   "what", "is", "about", "how", "why", "what"] + browse_check
  explain_start = "explain"
  summarize_check = ["summarize", "short", "brief", "and", "it",
                     "the", "results", "how", "why", "abut", "what"] + browse_check
  summarize_start = "summarize"
  
  def __init__(self, model_name): nltk.download(model_name)  # NOTE: e.g. "punkt"
  
  def check_greeting(self, prompt: str) -> bool: return any(keyword in nltk.tokenize.word_tokenize(prompt.lower()) for keyword in Triggers.greeting)
  
  def check_goodbye(self, text: str) -> bool: return any(keyword in nltk.tokenize.word_tokenize(text.lower()) for keyword in Triggers.goodbye) or all(keyword in nltk.tokenize.word_tokenize(text.lower()) for keyword in Triggers.goodbye_default_phrase)
  
  def check_browse_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower()) 
    return True if Triggers.browse_start in tokens and any(keyword in tokens for keyword in Triggers.browse_check) else False
  
  def check_explain_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return True if Triggers.explain_start in tokens and any(keyword in tokens for keyword in Triggers.explain_check) else False
  
  # TODO: find sentiment to play song or not
  def check_audio_request(self, text: str) -> bool:
    tokens = nltk.tokenize.word_tokenize(text.lower())
    return True if Triggers.audio_start in tokens and any(keyword in tokens for keyword in Triggers.audio_check) else False
