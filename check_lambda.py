import sys
import ast

def has_lambda(node):
    if isinstance(node, ast.Lambda):
        return True
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if has_lambda(item):
                    return True
        elif isinstance(value, ast.AST):
            if has_lambda(value):
                return True
    return False

def check_for_lambda(filename):
    with open(filename, "r") as f:
        code = f.read()
    tree = ast.parse(code)
    return has_lambda(tree)

# Check if there are any lambda functions in the staged Python files
staged_files = sys.argv[1:]
for filename in staged_files:
    if check_for_lambda(filename):
        print("Error: Lambda functions are not allowed in this repository.")
        exit(1)

exit(0)
