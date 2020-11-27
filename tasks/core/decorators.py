import requests
import functools
import logging

def timeout_request(_func=None,*, num_times=0):
    def decorator_timeout_request(func):
        @functools.wraps(func)
        def wrapper_timeout_request(*args,**kwargs):
            logging.getLogger('info_logger').info('Attempt to connect')
            response = func(*args,**kwargs)
            if response.status_code == 408:
                if num_times>0:
                    for _ in range(num_times):
                        logging.getLogger('info_logger').info('Retry attempt to connect')
                        r= func(*args,**kwargs)
                        if r.status_code != 408:
                            logging.getLogger('info_logger').info('Success')
                            return r
                logging.getLogger('info_logger').info('Failure')
                return response
            else:
                logging.getLogger('info_logger').info('Success')
                return response
    
        return wrapper_timeout_request

    if _func is None:
        return decorator_timeout_request
    else:
        return decorator_timeout_request(_func)
