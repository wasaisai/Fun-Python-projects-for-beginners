import sys

def prase_argv():
    if len(sys.argv) < 2:
        return None, None

    mode = None
    expr = None
    if sys.argv[1] == "--cli":
        mode = "cli"
        if len(sys.argv) > 2:
            expr = " " .join(sys.argv[2:])
    elif sys.argv[1] == "--gui":
        mode = "gui"
    
    return mode, expr
    
