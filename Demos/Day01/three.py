import ast
import astpretty
import dis
code = "print('hi')"
tree = ast.parse(code)

astpretty.pprint(tree)

code2 = "print('hello')"
compiled_code=compile(code,'<string>','exec')
dis.dis(compiled_code)