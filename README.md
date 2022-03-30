# lightcontrol
led light source interface/control software

## Build
```
python -m build --wheel
#python -m build --wheel --no-isolation
```

## Install
```
python -m installer --destdir="./someplace" dist/*.whl
```

## Test
### Manually
```
PYTHONPATH=someplace/usr/lib/python3.10/site-packages ./someplace/usr/bin/livechart-cli
#PYTHONPATH=someplace/usr/lib/python3.10/site-packages ./someplace/usr/bin/livechart
```
### With unittest
```
# (from the project root)
PYTHONPATH="src" python -m unittest -v

# with code coverage report
PYTHONPATH="src" coverage run --source livechart -m unittest -v; coverage report
```
## Build/Install Combo
```
rm -rf someplace/; rm -rf dist/; python -m build --wheel; python -m installer --destdir="./someplace" dist/*.whl
```
