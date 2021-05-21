#!/usr/bin/env python3
from idle_time import IdleMonitor
from logging import debug, info, basicConfig, INFO, DEBUG
from yaml import load, dump, FullLoader
from time import sleep
from sys import argv
from subprocess import Popen, PIPE, DEVNULL

# Using rivalcfg's cli


def is_idle() -> bool:
    """
    Checks if user is idle
    :return: True, if idle, False if not
    """
    debug(f"Idle time: {monitor.get_idle_time()}")
    return True if monitor.get_idle_time() > options['idle_timeout'] else False


def color_loop(command: str, color_list: list, delay: float) -> None:
    """
    Loops through colors from the list with delay
    :param command: rivalcfg command
    :param color_list: list of colors in hex to loop through
    :param delay: delay between each change in seconds
    :return: None
    """
    while not is_idle():
        for color in color_list:
            Popen([command, '--color', color], stderr=DEVNULL, stdout=DEVNULL)
            sleep(delay)


if __name__ == '__main__':

    monitor = IdleMonitor.get_monitor()

    if len(argv) > 1 and argv[1] == '-d':
        basicConfig(level=DEBUG, format='%(message)s')
        debug("Initialized")
    else:
        basicConfig(level=INFO, format='%(message)s')
        info("Initialized")
    try:
        with open('options.yml') as f:
            options = load(f, Loader=FullLoader)
    except FileNotFoundError:
        with open('options.yml', 'w') as f:
            dump({
                'rivalcfg_command': "python -m rivalcfg",
                'idle_color': "black",
                'idle_timeout': 30,
                'colors_delay': 0.5,
                'colors': ""
            }, f, sort_keys=False)
        raise SystemExit("Tweak values to your needs")
    info("Settings loaded!")
    debug(f"Options from yaml loaded: {options}")
    black_bool = False
    color_bool = True
    while True:
        if is_idle() and black_bool is False:
            idle = Popen([options['rivalcfg_command'], '--color', options['idle_color']], stderr=PIPE, stdout=PIPE)
            debug(f"Idle stdout: {idle.stdout}")
            black_bool = True
            color_bool = False
            debug(f"Idle mode, vars:\n black_bool: {black_bool}, color_bool: {color_bool}")
        if not is_idle() and color_bool is False:
            color_bool = True
            black_bool = False
            debug(f"Color mode, vars:\n black_bool: {black_bool}, color_bool: {color_bool}")
            color_loop(options['rivalcfg_command'], options['colors'], options['colors_delay'])
