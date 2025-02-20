from fastapi import FASTAPI
app= FASTAPI
@app.get("/predict")
def predict_model(age:int,sex:str):
  if age>15 or sex=='F':
    return("yes")
  else:
    return("no")
