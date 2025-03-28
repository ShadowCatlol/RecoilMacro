# RecoilMacro
Rainbow Six Siege macro that uses SteelSeries drivers.

# Config ⚙
A default config looks like so:
```
{
    "pulldown": true,
    "hold_mouse_down": true,
    "toggle_key": "`",
    "clicks_per_second": 100,
    "primary_pulldown_rate": 1.25,
    "secondary_pulldown_rate": 0.22,
    "configs": {
        "f1": 10,
        "f2": 2.4,
        "f3": 0.05,
        "f4": 0.4,
        "f5": 0.5,
        "f6": 0.6,
        "f7": 0.7,
        "f8": 0.8,
        "f9": 0.9,
        "f10": 1.0,
        "f11": 1.1,
        "f12": 1.2
    }
}
```

### `pull_down`
 - Wether or not the script will pull down to reduce recoil
### `hold_mouse_down`
 - Wether you need to hold down the mouse button to keep shooting, otherwise making it turn on and off with every click, This ussually feels the best so leave it on
### `toggle_key`
 - The key that will pause and resume the script
### `clicks_per_second`
 - The amount of clicks the script tries to do per second, good for semi automatic weapons. DO NOT PUT THIS OVER 300 BECAUSE THE SCRIPT WILL CRASH.
### `primary_pulldown_rate`
 - The pulldown rate the script uses when the `1` key is pressed, which switches to your primary
### `sceondary_pulldown_rate`
 - The pulldown rate the script uses when the `2` key is pressed, which switches to your secondary
### `configs`
 - When the specific key is pressed in the list the current pulldown rate is set to that number. This is good for having preset setups.
 - Ex: if I press `f12` with the default config from earlier then the pulldown rate is gonna be set to f12

# Usage 🤖

Make sure python is installed then just, run autoclicker.py and it'll automatically install any dependencies.
