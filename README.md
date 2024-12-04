# VDMA-LIF JSON Parsers

This repository provides **JSON parsers** and models for the **VDMA - LIF (Layout Interchange Format)**, 
which is used for defining track layouts and exchanging information between the integrator of driverless transport vehicles and a third-party master control system.


The repository contains:
- A **JSON Schema** that defines the structure of the VDMA-LIF format: [lif-schema.json](schema/lif-schema.json).
  The schema is based on the Version 1.0.0 [guidline document](https://vdma.org/documents/34570/3317035/FuI_Guideline_LIF_GB.pdf). 
- **Parsers and models** written in:
    - **Python**
    - **C#**
    - **TypeScript**

The models are generated from the [lif-schema.json](schema/lif-schema.json) using [quicktype](https://quicktype.io/).

All package are available through the standard package managers.

## Usage

### Python
Add [vdma-lif](https://pypi.org/project/vdma-lif/) package

```bash
pip install vmda_lif
```
Usage:
```python
from vdma_lif.parser import LIFParser
layout_collection = LIFParser.from_file("example.lif.json")
```

### C#
Add [Vdma.Lif](https://www.nuget.org/packages/Vdma.Lif) package
```
dotnet add package Vdma.Lif
```

Usage:
```csharp
LifLayoutCollection layoutCollection = LifJsonParser.FromJson(lifJson);
```

### JavaScript / TypeScript

Add [vmda-lif](https://www.npmjs.com/package/vdma-lif) package

```bash
npm install --save-dev vdma-lif
```

Usage:
```typescript
import { LIFParser } from 'vdma-lif';

const layoutCollection = LIFParser.fromJson(jsonString)
```

## Generate Models

Install dependencies
```
npm install
```

### Python
### Dependencies
- Python >=3.7
- Build requirements: 
  In `src/python` run
    ```
    pip install .[dev]
    ```

### Generate
```
npm generate:python
```

## C#
### Dependencies
- .NET 8.0
- Install Resharper CLI
    ```
    dotnet tool install -g JetBrains.ReSharper.GlobalTools
    ```
### Generate
```
npm generate:csharp
```

## TypeScript

### Dependencies
- Install npm
- In `src/typescript` run
    ```
    npm install
    ```
### Generate
```
npm generate:typescript
```

### Dependencies

### Generate

## Contributing

Contributions are welcome! If you want to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new **Pull Request**.

Please ensure all changes are covered by unit tests.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

Let me know if you need any further adjustments!

## Maintainers

This repository is maintained by Continua Systems GmbH. For any inquiries, please contact us at:

* Website: https://continua.systems
* Email: info@continua.systems

