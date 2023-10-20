from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    optional: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}



# send 201 status code when post is created by default it is 200
@app.post("/create_post", status_code=status.HTTP_201_CREATED)
# the ... is a python3 feature called Ellipsis. It is used to indicate that the parameter is required.
# async def create_post(payLoad: dict = Body(...)):
async def create_post(post: Post):
    print(post)
    print(dict(post))
    return {"message": "Post created successfully"}


@app.get("/get_post/latest")
async def get_latest_post():
    return {"message": "Latest post"}


@app.get("/get_post/{post_id}")
async def get_post(post_id: int, response: Response):
    if post_id > 10:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Post not found"}
        raise HTTPException(
            status_code=404, detail=f"Post number {post_id} not found")
    return {"message": f"Post id is {post_id}"}

@app.delete("/delete_post/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    # code
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    