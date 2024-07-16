from fastapi import FastAPI
from workout_api.routers import api_router 

app = FastAPI(title='WorkoutAPI')

app.include_router(api_router)

# if __name__ == 'main':
#     import uvicorn

#     uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True) #não precisa pq usamos o make file, então damos apenas o comando make run