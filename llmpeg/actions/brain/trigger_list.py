from dataclasses import dataclass


@dataclass
class TriggerList:
  audio_check = ['from', 'by', 'song', 'music', 'play']
  audio_start = 'play'
  goodbye = ['bye', 'goodbye']
  greeting = ['hi', 'hello', 'hey', 'greetings']
  goodbye_default_phrase = ['see', 'you', 'next', 'time']
  browse_check = [
    'search',
    'browse',
    'find',
    'lookup',
    'read about',
    'look up',
    'research',
    'explore',
    'investigate',
    'investigation',
    'study',
    'examine',
    'inspect',
    'scrutinize',
    'analyze',
  ]
  browse_start = 'browse'
  explain_check = [
    'explain',
    'and',
    'it',
    'the',
    'results',
    'what',
    'is',
    'about',
    'how',
    'why',
    'what',
  ] + browse_check
  explain_start = 'explain'
  summarize_check = [
    'summarize',
    'short',
    'brief',
    'and',
    'it',
    'the',
    'results',
    'how',
    'why',
    'abut',
    'what',
  ] + browse_check
  summarize_start = 'summarize'
