from unittest.mock import patch

import pytest

from llmpeg.agent import Agent

def test_default_agent():
  agent = Agent('conversation_model', 'nlp_model', 'tts_model_size', 'stt_model_size')
  test_ocr(agent)

def test_ocr(agent: Agent):
  data = agent.ocr_url("https://example.com/")
  assert data == ['Example Domain', 'This domain isfor use in illustrative examplesin documents. You', 'use this', 'domain in literature without prior coordination or asking for permission.', 'More information..', 'may']
  