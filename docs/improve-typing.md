Since [Queries][edgeql_queries.queries.Queries] are dynamically generated at runtime, th
ey cannot provide type hints for your editors/IDEs or linters. But you can write typings 
for your queries yourself.

`queries.edgeql`:
```edgeql
{!./src/improve-typing/impove_typing0.edgeql!}
```

And python code:
```python3
{!./src/improve-typing/impove_typing0.py!}
```