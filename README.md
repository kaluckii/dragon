### Installation:
Add next dependency to `pyproject.toml`:
```toml
[tool.poetry.dependencies]
dragon = { git = "ssh://git@github.com/kaluckii/dragon.git", branch = "main" }
```

Then, run `poetry install` and package will be installed.

### Use example:
Build Aiogram keyboard with list of tuples:

```python
from dragon.tools.helpers import build_keyboard

keyboard = build_keyboard([('keyname', 'keycallback'), ('url', 'https://github.com')])
```