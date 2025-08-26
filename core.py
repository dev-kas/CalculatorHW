workspace = ""
is_workspace_the_result = False

def set_workspace(w, is_result=False):
    global workspace
    global is_workspace_the_result
    is_workspace_the_result = is_result
    workspace = w

def write_workspace(w):
    global workspace
    workspace += w

def get_workspace():
    return workspace

def map_token(tok):
    if tok in ''.join(str(i) for i in range(0, 10)): return str(tok)
    if tok in "()*/+-%": return f" {tok} "
    if tok == ".": return tok
    if tok == "^": return "**"
    raise Exception(f"Unknown token: {tok}")

def run():
    wk = get_workspace()
    set_workspace("") # clear workspace
    try:
        code = "".join(map(map_token, wk))
        result = eval(code)
    except Exception as e:
        set_workspace(str(e), is_result=True)
        return
    set_workspace(str(result), is_result=True)
