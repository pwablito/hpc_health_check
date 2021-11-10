# HPC Health Check

A system for checking the health of HPC clusters.

All subcommands:
```
usage: Perform a health check [-h] {test,file,local,ssh} ...

positional arguments:
  {test,file,local,ssh}

optional arguments:
  -h, --help            show this help message and exit
```

Health check subcommands:
```
usage: Perform a health check {file,local,ssh} [-h]
                                               [--out {json,yaml,xml}]
                                               filename

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  --out {json,yaml,xml}
                        Output format
```

To run unit tests: `./health_check.py test`


Created by [BYU HPC](https://github.com/BYUHPC) employees [Paul Spencer](https://github.com/pwablito) and [Joseph du Toit](https://github.com/jcdutoit)
