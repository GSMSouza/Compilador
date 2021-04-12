from analyzer.lexical import tokenize


def main():
    code = '''
    procedure um (a, g: real; d, c: integer)\n
  var h, i, j: real;
  var l: integer
begin
  h := 2.0;
  a := g + 3.4 / h;
  l := c - d * 2;
  if (c+d)>=5 then
    write(a)
  else
    write(l)
    '''
    print(tokenize(code))


if __name__ == '__main__':
    main()
