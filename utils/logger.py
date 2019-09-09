import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s %(asctime)s.%(msecs)03d %(module)10s/%(lineno)-5d %(message)s'
)

log = logging.getLogger()
