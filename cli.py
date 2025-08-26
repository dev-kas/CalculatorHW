import core

def main():
    while True:
        expr = input("> ")
        if expr == "exit": break
        core.set_workspace(expr)
        core.run()
        output = core.get_workspace()
        if core.is_workspace_the_result:
            output = f"< {output}"
        print(output)
