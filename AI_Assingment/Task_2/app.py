from fastapi import FastAPI
from pydantic import BaseModel
from model import suggest_recipe

app = FastAPI(title="Recipe Chatbot API")

class IngredientsInput(BaseModel):
    ingredients: list[str]

@app.post("/chat")
def chat(input: IngredientsInput):
    recipe = suggest_recipe(input.ingredients)

    if recipe:
        return {
            "recipe": recipe["recipe"],
            "steps": recipe["steps"]
        }
    else:
        return {
            "message": "No matching recipe found."
        }
