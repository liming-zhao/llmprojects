from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
file_path = pathlib.Path('C:\\Users\\linac\\Documents\\clearinghouse.pdf')
file_path2 = pathlib.Path('C:\\Users\\linac\\Documents\\Lecture6.pdf')
file_path3 = pathlib.Path('C:\\Users\\linac\\Documents\\SiPJanuary2025_TinkercadandScratch.pdf')


# Upload the PDF using the File API
sample_file1 = client.files.upload(
  file=file_path,
)
sample_file2 = client.files.upload(
  file=file_path2,
)
sample_file3 = client.files.upload(
  file=file_path3,
)


prompt="Summarize this document"

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_file1, sample_file2, sample_file3, "can you classify the documents into 2 categories, and naming each of the category"])
print(response.text)