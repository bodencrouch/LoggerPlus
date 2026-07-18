# loggerplus

Rotating file logs that don't fall over when you have more than one process writing.

`RobustLogger` is the main entry. There's also `format_exception_with_variables` if you want stack traces with locals in them.

## Install

```bash
pip install git+https://github.com/bodencrouch/LoggerPlus.git
# or
pip install -e .
```

PyPI still has an older 0.1.3 under the same name. This tree is **0.2.0**: no external `utility.*` imports, and default log files are named `loggerplus*.log`.

```python
from loggerplus import RobustLogger

log = RobustLogger()
log.info("hello")
```

## License

LGPL-3.0-or-later

Repo on GitHub: [bodencrouch/LoggerPlus](https://github.com/bodencrouch/LoggerPlus).
