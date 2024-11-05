# VDMA-LIF JSON Parsers

JSON parsers and models for the VDMA - LIF (Layout Interchange Format), which is used for defining track layouts and exchanging information between the integrator of driverless transport vehicles and a third-party master control system.

The models are generated from a json schema which can be found in the [vdma-lif repository](https://github.com/continua-systems/vdma-lif.git).

## Install

```bash
pip install vmda_lif
```

## Usage

### Read layouts from file
```python
from vdma_lif.parser import LIFParser
layout_collection = LIFParser.from_file("example.lif.json")
```

### Read layouts from string
```python
from vdma_lif.parser import LIFParser
layout_collection = LIFParser.from_json(layout_collection_str)
```

### Convert into json
```
layout_collection_str = LIFParser.to_json(layout_collection)
```

### Write layouts to file:
```python
LIFParser.to_file(layout_collection, "example.lif.json")
```

## License

This project is licensed under the **MIT License**.

## Maintainers

This repository is maintained by Continua Systems GmbH. For any inquiries, please contact us at:

* Website: https://continua.systems
* Email: info@continua.systems