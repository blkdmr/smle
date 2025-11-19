import traceback

from smle.args import read_configuration_file
from smle.logging import init_logging_module, close_logging_module

def smle(main_func):
    def inner():
        args = read_configuration_file()
        init_logging_module(args)

        try:
            return main_func(args)
        except Exception:
            print(traceback.format_exc())
        finally:
            close_logging_module()
    return inner
