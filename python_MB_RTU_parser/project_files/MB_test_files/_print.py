import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
# log.setLevel(logging.DEBUG)


def _print(value):
    if hasattr(value, "bits"):
        t = value.bits
    elif hasattr(value, "registers"):
        t = value.registers
    else:
        log.error(value)
        return
    log.info("Printing : -- {}".format(t))
    return t
