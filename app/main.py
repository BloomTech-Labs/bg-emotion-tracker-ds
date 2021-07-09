from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import viz


description = """To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

APP = FastAPI(
    title='DS API - Boys & Girls Club',
    description=description,
    docs_url='/',
    version='0.36.0',
)

APP.include_router(viz.router, tags=['Visualization'], prefix="/vis",)

APP.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(APP)
