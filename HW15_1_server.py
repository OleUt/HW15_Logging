import socket
import logging

logging.basicConfig()
logger = logging.getLogger('server')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('new.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5000))
sock.listen(5)
sock.settimeout(None)

logger.info('server is up')
logger.warning('max backlog number is 5')


while True:
    conn, addr = sock.accept()
    logger.info(f"connection from {addr} has been established")
    a = None

    try:
        conn.settimeout(10)
        a = conn.recv(1024)
    except TimeoutError:
        logger.warning('time is over')
    finally:
        if not a and TimeoutError:
            logger.error('no data')
            conn.send(bytes('Sorry, time is over and no data have been entered.', encoding='UTF-8'))
        else:
            logger.info('client send a message')
            conn.send(bytes('Congrats! Your text is accepted.', encoding='UTF-8'))
