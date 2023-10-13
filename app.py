import os
import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
import uuid
from dotenv import load_dotenv

load_dotenv()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key= os.environ.get("OPENAI_API_KEY"),
                model_name="text-embedding-ada-002"
            )

client = chromadb.PersistentClient(path=os.environ.get("CHROMA_PATH"))
collection = client.get_or_create_collection(name=os.environ.get("CHROMA_COLLECTION_NAME"), embedding_function=openai_ef)

def create_table_data(data):
    table_data = []

    for i in range(len(data['ids'])):
        id_value = data['ids'][i] if data['ids'] is not None and i < len(data['ids']) else ""
        embedding = data['embeddings'][i] if data['embeddings'] is not None and i < len(data['embeddings']) else ""
        dokument = data['documents'][i] if data['documents'] is not None and i < len(data['documents']) else ""

        row = {
            'ID': id_value,
            'Embedding': embedding,
            'Dokument': dokument
        }
        table_data.append(row)

    return table_data

def create_document(doc_content):
    myuuid = uuid.uuid4()
    collection.add(
        documents=doc_content,
        ids=str(myuuid),
    )

def delete_document(doc_uuid):
    collection.delete(ids=doc_uuid)    

def main():
    st.set_page_config(
        page_title="QuickHelpViewer", page_icon=":swan:")

    st.header("QuickHelp Chroma DB Query :swan:")

    if st.button("Run Query"):
        # Embeddings are not returned due to performance reasons
        # data = collection.get(include=['embeddings', 'metadatas', 'documents' ])
        data = collection.get(include=['metadatas', 'documents' ])
        st.title('Data Table')
        st.table(create_table_data(data=data))
        
    selected_id = st.text_area("Enter the id of the document")

    if st.button("Delete") and selected_id:
        delete_document(selected_id)
        st.info("Query send")

    st.header("Add Documents :newspaper:")   
    
    doc_content = st.text_area("Document Content")    

    if st.button("Add") and doc_content:
       create_document(doc_content)
       st.info("Query send")

if __name__ == '__main__':
    main()