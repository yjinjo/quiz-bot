from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/file/info")
async def get_file_info(file: UploadFile = File(...)):
    contents = await file.read()

    return {
        "content_type": file.content_type,
        "filename": file.filename
    }

