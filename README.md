DevOps Lab 2020 summer

# description of the package
This package monitor state of system (CPU load, memory usage and virtual memory usage) and can create log file in txt or json format.

# install instruction
pip install .

# use instruction
snapshot -h # help
snapshot -i <interval> -t <type> # i - interval (seconds, default = 30), t - file type (txt or json, default = json)

# uninstall instruction
pip uninstall monitoring