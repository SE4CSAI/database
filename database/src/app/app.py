from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI(title= "add to database")

# End point for saving files to a database to update the model
@app.post("/upload_image")
def upload_image(file : UploadFile = File(...)):
    try:
        contents = file.file.read()
        suffix = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        with open(file.filename +'_' + suffix + '.jpg', 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message" : "There was an error uploading the file"}
    finally:
        file.file.close()
