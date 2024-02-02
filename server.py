from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import StreamingResponse


app = FastAPI()
client = OpenAI()

def generator(msg: str):
    result = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
        model="gpt-3.5-turbo",
        stream=False,
    )

    return result.choices[0].message.content


@app.get("/")
def main(msg):
    return StreamingResponse(generator(msg))
