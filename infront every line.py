import textwrap
n='''Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
'''
text=textwrap.dedent(n)
te=textwrap.fill(n, width=50)
final=textwrap.indent(te, '>')

print(final)