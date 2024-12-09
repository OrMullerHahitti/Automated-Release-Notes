import httpx
async def make_request(url:str,method:str='GET',headers:dict=None,data:dict=None):
    async with httpx.AsyncClient() as client:
        if method=='GET':
            response = await client.get(url,headers=headers)
        elif method=='POST':
            response = await client.post(url,headers=headers,json=data)
        else:
            raise ValueError(method)
        response.raise_for_status()