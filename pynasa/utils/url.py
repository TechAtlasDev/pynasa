def joinURL(url:str, *args) -> str:
    for arg in args:
        url += '/' + arg
    return url