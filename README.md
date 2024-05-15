# PDF-chatbot
This is a customized chatbot with RAG implementation, that works on custom documents.
This project consists of 5 Python files and 1 source pdf("48lawsofpower.pdf")
Code files are:
  1. requirements.txt (contains a list of all the required libraries and resources)
  2. prepareMD.py (this ".py" file creates a ".md" file out of the ".pdf" source file)
  3. create_db.py (this file creates a serverless vector database to store vectors and embeddings)
  4. compare_embeddings.py (this file extracts the context for an answer by calculating "pairwise_embedding_distance" which is further fed to the LLM model to generate a response)
  5. query_data.py (finally this file allows the user to interact with the document and provides the answer as well as the context of that answer, we can also deploy this file as a web app)

     **THANK YOU**     **:)**
