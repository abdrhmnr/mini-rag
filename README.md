# mini-rag
This is a minimal implementation of the RAG model for question answering .

## Requirements 
 - Python 3.8 or later 
 #### Install Python using MiniConda 

1) Download and install MiniConda 
2) Create a new environment Using thr following command:
```bash 
$ conda create -n mini-rag python= 3.8 
```
3) Activate the environment :
```bash 
$ conda activate mini-rag
```
# Installation
### Install the required packages
```bash 
$ pip install -r requirements.txt
```
### Setup the environment variables
```bash 
$ cp .env.example .env
```
## Run the FastAPI server
```bash 
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


