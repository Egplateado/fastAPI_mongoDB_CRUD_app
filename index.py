# import statements
from  fastapi import FastAPI
from routes.student import student_router
#create APP
app = FastAPI()
#register your router
app.include_router(student_router)


