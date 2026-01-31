from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

BACKENDS = {
    "service-a": "http://localhost:9001",
    "service-b": "http://localhost:9002",
}

@app.api_route("/{service}/{path:path}",
               methods=["GET", "POST", "PUT", "DELETE"])
async def reverse_proxy(service: str, path: str, request: Request):
    if service not in BACKENDS:
        return Response("Unknown service", status_code=404)

    target_url = f"{BACKENDS[service]}/{path}"

    async with httpx.AsyncClient() as client:
        proxy_request = client.build_request(
            method=request.method,
            url=target_url,
            headers=dict(request.headers),
            content=await request.body()
        )

        proxy_response = await client.send(proxy_request)

    return Response(
        content=proxy_response.content,
        status_code=proxy_response.status_code,
        headers=dict(proxy_response.headers),
    )

