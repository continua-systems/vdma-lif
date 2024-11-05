# VDMA-LIF JSON Parsers

JSON parsers and models for the VDMA - LIF (Layout Interchange Format), which is used for defining track layouts and exchanging information between the integrator of driverless transport vehicles and a third-party master control system.

The models are generated from a json schema which can be found in the [vdma-lif repository](https://github.com/continua-systems/vdma-lif.git).

## Install

```bash
dotnet add package Vdma.Lif
```

## Usage

### Read layouts from file
```csharp
LifLayoutCollection layoutCollection = LifJsonParser.FromJson(lifJson);
```

### Read layouts from string
```csharp
LifLayoutCollection layoutCollection = LifJsonParser.FromFile(jsonFilePath);
```

### Convert layouts into json
```csharp
string lifJson = layoutCollection.ToJson();
```

### Write layouts to file:
```csharp
layoutCollection.ToFile(jsonFilePath);
```

## License

This project is licensed under the **MIT License**.

## Maintainers

This repository is maintained by Continua Systems GmbH. For any inquiries, please contact us at:

* Website: https://continua.systems
* Email: info@continua.systems