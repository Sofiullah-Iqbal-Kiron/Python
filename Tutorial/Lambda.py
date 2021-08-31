# A lambda is small anonymous one-liner function that can have many parameters as it's argument.
# Lambda function is defined with "lambda" keyword.
# lambda arguments : expression
# Value obtained by this expression will returned from this lambda.
# The power of lambda is better shown when we use them as an anonymous function inside another function.

# Assume a function y = x * x
y = lambda x: x ** 2
print(y(3))

# Here y is dependent on a lambda so that we need to pass
# arguments of that lambda through it inside a set of parenthesis.
