from app import web
from settings import HOST, PORT, DEBUG

if __name__ == '__main__':
    web.run(host=HOST, port=PORT, debug=DEBUG)