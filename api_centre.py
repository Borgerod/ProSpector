# from django.db import models 





''' TODO __________________________
	- [ ] generate api keys on AWS
	- [ ] store api keys on a PG table (if AWS doesnt handle it by itself)
	- [ ] create verification code for API keys to gatekeep API-calls (if AWS doesnt handle it by itself)
	- [ ] create functions for API-actions
'''

def getCallList():
	pass







# from django.shortcuts import render

# def index(request):
#    return render(request, 'index.html')

# def home(request):
#    msg = request.GET.get('message')
#    return render(request, 'home.html',{'msg':msg })



# from django.shortcuts import render

# def index(request):
#     user = {
#         'fullname' : request.user.get_full_name(),
#         'firstname' : request.user.first_name,
#         'lastname' : request.user.last_name,
#         'email' : request.user.email,
#         'last_login': request.user.last_login,
#         'account_created': request.user.date_joined
#     }
#     return render(request, 'index.html',{'user':user})

# index(request)





from fastapi import FastAPI, Depends, Request, Form, status 
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates


app = FastAPI()

@app.get("/")
def home():
	return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
	return {"item_id": item_id}
	
home()
read_item(10)

# def home(request: Request, db: Session=Depends(get_db)):
# 	todos = db.query(models.Todo).all()
# 	return templates.TemplateResponse("base.html", "request":request, "todo_list": todos)