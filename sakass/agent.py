
# import pprint
# from langchain_community.document_loaders import AsyncChromiumLoader
# from langchain_community.document_transformers import BeautifulSoupTransformer
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.chains import create_extraction_chain

from .capabilities import Speak, Listen
from .modules import Conversation, Browser

class Agent:
  # summarize_schema = {
  #       "properties": {
  #           "news_article_title": {"type": "string"},
  #           "news_article_summary": {"type": "string"},
  #       },
  #       "required": ["news_article_title", "news_article_summary"],
  #   }
  
  def __init__(self, conversation_model, browser_model):
    self.conversation_model = conversation_model
    self.browser_model = browser_model

    self.conversation = Conversation(model=self.conversation_model)
    self.browser = Browser(model=self.browser_model)

    self.speak = Speak()
    self.listen = Listen()
    

  def respond(self, text):
    print(self.conversation.respond(text))

  def summarize(self, text):
    print(self.conversation.summarize(text))
  
  # def extract(self, content: str, schema: dict):
  #   return create_extraction_chain(schema=schema, llm=self.think).run(content)
  
  # def scrape_with_playwright(self, urls, schema):
  #     loader = AsyncChromiumLoader(urls)
  #     docs = loader.load()
  #     bs_transformer = BeautifulSoupTransformer()
  #     docs_transformed = bs_transformer.transform_documents(
  #         docs, tags_to_extract=["span"]
  #     )
  #     # Grab the first 1000 tokens of the site
  #     splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  #       chunk_size=1000, chunk_overlap=0
  #     )
  #     splits = splitter.split_documents(docs_transformed)
  #     # Process the first split
  #     extracted_content = self.extract(schema=schema, content=splits[0].page_content)
  #     pprint.pprint(extracted_content)
  #     return extracted_content

  def summarize_url(self, url):
    print("oops, under development")
    # urls = [url]
    # extracted_content = self.scrape_with_playwright(urls, schema=self.summarize_schema)
    # self.summarize(extracted_content) 
