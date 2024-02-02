# Sample OpenAI SSE Engine

This is an openai SSE (server side engine) example that accepts curl commands against a local server.
You can issue commands such as

```
curl -X 'GET' \
  'http://127.0.0.1:8000/?msg=who%20are%20you%3F' \
  -H 'accept: application/json'
```

It uses a FastAPI engine - https://fastapi.tiangolo.com/
This code uses an ASGI service called uvicorn.
https://www.uvicorn.org/

To get started:

1. git clone this repo
2. .venv/bin/activate (if on windows, create new venv)
3. pip install -r requirements.txt
4. set OPENAI_API_KEY to your key
5. uvicorn server.app --reload
6. execute the curl code against this, or go to localhost:8000/docs to get swagger


To do:
1. Add streaming output
2. Add Playground UI

