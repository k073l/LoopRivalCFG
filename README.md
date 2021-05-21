# LoopRivalCFG
Just a simple automation script for rivalcfg

### Usage
- Install requirements with pip (`pip3 install -r requirements.txt`)
- If on linux, according to [rivalcfg's docs](https://flozz.github.io/rivalcfg/install.html) run `sudo rivalcfg --update-udev`
- Run `main.py` to generate `options.yml`
- Tweak them to your liking (colors must be in hex)

Example `options.yml`:
```yaml
rivalcfg_command: rivalcfg
idle_color: black
idle_timeout: 30
colors_delay: 0.5
colors:
  - FF2D00
  - FF6C00
```
- Run `main.py` again or add it to cron (or similar)

It is possible you may encounter lags in your mouse movement for first few seconds to minute from running the script and allowing it to start the color loop.

---

Thanks to flozz for creating [rivalcfg](https://github.com/flozz/rivalcfg)