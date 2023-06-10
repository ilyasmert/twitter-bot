import os
import openai
openai.organization = "<ORGANIZATION_ID>"
openai.api_key = "<OPENAI_API_KEY>"
openai.Model.retrieve("gpt-4")
