# VDMA-LIF JSON Parsers

JSON parsers and models for the VDMA - LIF (Layout Interchange Format), which is used for defining track layouts and exchanging information between the integrator of driverless transport vehicles and a third-party master control system.

The models are generated from a json schema which can be found in the [vdma-lif repository](https://github.com/continua-systems/vdma-lif.git).

## Install

```bash
npm install -D vdma-lif
```

## Usage

### Read layouts from file
```typescript
import { LIFParser } from 'vdma-lif';

const layoutCollection = LIFParser.fromFile(sampleFile);
```

### Read layouts from string
```typescript
const layoutCollection = LIFParser.fromJson(invalidJson)
```

### Convert into json
```typescript
const jsonString = LIFParser.toJson(layoutCollection)
```

### Write layouts to file:
```typescript
LIFParser.toFile(layoutCollection, "example.lif.json")
```

## License

This project is licensed under the **MIT License**.

## Maintainers

This repository is maintained by Continua Systems GmbH. For any inquiries, please contact us at:

* Website: https://continua.systems
* Email: info@continua.systems