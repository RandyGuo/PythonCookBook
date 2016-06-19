from decimal import Decimal

a = Decimal('1.3')
b = Decimal('1.7')

print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

