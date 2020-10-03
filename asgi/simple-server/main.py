import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request


async def factorial(request: Request):
    n = request.query_params.get('n', 1)

    await asyncio.sleep(int(n))

    return JSONResponse({'result': 'world'})

routes = [
    Route('/factorial', factorial)
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, http='h11', loop='asyncio')
