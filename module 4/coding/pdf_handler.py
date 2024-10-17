from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader(
    "./HydrogenFuel.pdf"
)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False
)

chunks = []

for i in docs:
    text = i.page_content
    peices = text_splitter.create_documents([text])
    chunks.extend(peices)

print(chunks[0])
print(len(chunks))