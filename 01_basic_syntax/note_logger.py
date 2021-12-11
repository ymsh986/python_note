# coding: utf-8

def set_logger():
    from logging import getLogger, StreamHandler, Formatter, DEBUG
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(DEBUG)

    # フォーマッタを定義する（第一引数はメッセージのフォーマット文字列、第二引数は日付時刻のフォーマット文字列）
    fmt = Formatter("%(asctime)s-%(funcName)s[%(levelname)s]%(lineno)s:%(message)s", "%Y-%m-%dT%H:%M:%S")
    handler.setFormatter(fmt)

    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def output_general_logs(func):

    def _wrapper(*args, **kwargs):
        logger.debug(f'===== {func.__name__} start. =====')
        result = func(*args, **kwargs)
        logger.debug(f'===== {func.__name__} end.   =====')
        return result

    return _wrapper


@output_general_logs
def func1(logger, arg1):
    logger.debug(arg1)


@output_general_logs
def func2(logger, arg1):
    logger.debug(arg1)


if __name__ == "__main__":
    logger = set_logger()
    func1(logger, "hello")
    func2(logger, "bye")
