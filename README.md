# ChromaDBToolkit
I developed this tool as I couldn't find a suitable solution for viewing, deleting, or adding entries to my Chroma database.

## Configuration

1. **Creating a Configuration File**:
   Create a file named `.env` in the root directory of the project. Add the following parameters and adjust the values accordingly:

    ```plaintext
    OPENAI_API_KEY=Your_OpenAI_API_Key
    CHROMA_PATH=Path_to_Database
    CHROMA_COLLECTION_NAME=Name_of_Collection
    ```
2. **Packages**:
   Intall all packages listed in the requirements.txt file.
   
## Instructions

Follow the steps in the [Configuration](#configuration) section to properly set up the tool. Once configured, you can use the tool to manage your Chroma database.

Run the programm with following command in the project root folder:
```plaintext
streamlit run app.py
```
