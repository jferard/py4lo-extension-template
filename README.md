# Py4LO Extension Template

Copyright (C) J. Férard 2023

Py4LO Extension Template is a template for Python extensions for LibreOffice and 
a script to pack and install the extension.

License : 
* the script is under GNU GPL v3.
* the extension template itself is beerware.
* the icon is LibreOffice Calc icon, under MPL v2.0 (if I'm not mistaken).

## Configuration
Needs `pytest` and `flake8`.

```
$ python3 -m pip install -r requirements.txt
```

## Usage
First, use the template to create the actual extension.
Hint : search all "MyExtension", "myMethod", "myself" in the src directory and make the necessary changes. 

Second, use:
```
$ python3 py4lo_extension_builder.py test
$ python3 py4lo_extension_builder.py create
```

And install the extension (double click on the .oxt file).

Or :
```
$ python3 py4lo_extension_builder.py install
```

## Sources and references
* https://github.com/luane-aquino/helloworld-libreoffice-extension
* https://github.com/smehrbrodt/libreoffice-starter-extension
* https://wiki.documentfoundation.org/Documentation/DevGuide/Writing_UNO_Components
* https://wiki.openoffice.org/wiki/UNO_component_packaging
* https://flywire.github.io/lo-p/45-UNO_Components.html
