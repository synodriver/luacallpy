# from redis import Redis, ResponseError
# import requests
# from loguru import logger
# # c = Redis(host='119.29.181.106',port=6380,password='215616',max_connections=1)
# try:
#     c = Redis(host='119.29.181.106',password='JJjj1283148',port=6380,socket_connect_timeout=10,single_connection_client=False)
# except:
#     pass
# for i in range(1):
#     try:
#         logger.info('send')
#         print(c.info())
#         # requests.get('http://127.0.0.1:9001')
#     except Exception as e:
#         print(e)
#         pass
def testfunc(a, b):
    return a * b + a*2
