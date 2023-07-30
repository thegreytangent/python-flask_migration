from config import app, db
from models import *





def all():
    return db.session.query(Post).all()

@app.route("/")
def index():
   posts = all()
   html = ""
   if len(posts):
    for post in posts:
        html = html + f"<div><h1>{post.title}</h1><p>{post.content}</p><hr></div>"
 
    return html

def create():
    post = Post(
        title="new post", 
        content="content post"
    )
    db.session.add(post)
    db.session.commit()
    print("Create post")

if __name__ == "__main__":  
    app.run(debug=True)
