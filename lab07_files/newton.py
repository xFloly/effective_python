from argparse import ArgumentParser, Namespace
import sympy as sp

parser = ArgumentParser()

parser.add_argument("function", help="function to find root")
parser.add_argument("-s", "--start", help="start point", type=float)
parser.add_argument("-i", "--iterations", help="iterations count, default = 100", type=int, default=100)
parser.add_argument("-e", "--epsilon", help="epsilon, default = 0.0001", type=float, default=0.0001)

args: Namespace = parser.parse_args()

x = sp.Symbol('x')
f = sp.sympify(args.function)
df = sp.diff(f, x)
x0 = args.start
x1 = x0
for i in range(args.iterations):
    if df.subs(x, x0) == 0:
        print("Derivative is zero")
        break
    x1 = x0 - f.subs(x, x0) / df.subs(x, x0)
    if abs(x1 - x0) <= args.epsilon:
        print(f"Found root at {x0} after {i} iterations")
        break
    x0 = x1

if abs(x1 - x0) > args.epsilon:
    print(f"Root not found after {args.iterations} iterations")
