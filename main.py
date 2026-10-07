from fastapi import FastAPI
from pydantic import BaseModel
import re 
app = FastAPI()
class TextData(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_text(data: TextData):
        word_count= len(data.text.split())

        character_count = len(data.text)
        sentence_count = len(re.findall(r'[.!?]',data.text))
        unique_word_count=data.text.split()
        uppercase_text=data.text.upper()
        lowercase_text=data.text.lower()
        average_word_length=round(sum(len(word)for word in unique_word_count)/len(unique_word_count),2)
        return{
            "word_count": word_count,
            "character_count": character_count,
            "sentence_count": sentence_count,
            "unique_word_count": unique_word_count,
            "uppercase_text":uppercase_text,
            "lowercase_text":lowercase_text,
            "average_word_length":average_word_length
        }