# GraphQL is the data query and manipulation language the api
# GraphQL is the more flaxible efficiente as compared to rest



import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry.field_extensions
import strawberry.types
@strawberry.type   # in order to ingrate GraphQl with a fastapi app, first decorate a python class as strawberry type.
class Book:
    title:str
    authoe:str
    price:int
@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:  # we create here book name function to we want to create the value in class
        return Book(title="Data Analyst",author="Prakash Abhale",price=500)
schema = strawberry.Schema(query=Query)   # use this query class as the parameter to obtain strawbwrry schema object
graphql_app=GraphQL(schema)
app=FastAPI()
app.add_route("/book",graphql_app)   #add routes to the fastapi object and run the server.  # this function alrady in strawberry
app.add_websocket_route("/book",graphql_app)  

#  http://127.0.0.1:8000/book

# # To run the server, use the following command in the terminal:
# # uvicorn main:app --reload



# pip install strawberry-graphql
