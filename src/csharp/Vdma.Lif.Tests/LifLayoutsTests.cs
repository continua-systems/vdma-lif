using System.Globalization;
using System.Text.Json;

namespace Vdma.Lif.Tests;

public class LifLayoutsTests
{
    // Define the path to the test JSON file
    private const string TestJsonFilePath = "example.lif.json";

    [Fact]
    public void FromFile_ValidJsonFile_ReturnsLifLayouts()
    {
        var lifLayouts = LifJsonParser.FromFile(TestJsonFilePath);

        AssertLayoutCollection(lifLayouts);
    }

    [Fact]
    public void FromJson_InvalidJson_ThrowsJsonException()
    {
        const string invalidJson = "{ invalid json }";

        Assert.Throws<JsonException>(() => LifJsonParser.FromJson(invalidJson));
    }

    [Fact]
    public void FromFile_NonExistentFile_ThrowsFileNotFoundException()
    {
        const string nonExistentFilePath = "nonexistent.json";

        Assert.Throws<FileNotFoundException>(() => LifJsonParser.FromFile(nonExistentFilePath));
    }

    [Fact]
    public void ToFile_ValidJsonFile_ContentSaved()
    {
        var layoutCollection = LifJsonParser.FromFile(TestJsonFilePath);

        AssertLayoutCollection(layoutCollection);

        var fileName = Path.GetTempFileName();

        layoutCollection?.ToFile(fileName);

        var layoutsFromFile = LifJsonParser.FromFile(fileName);

        AssertLayoutCollection(layoutsFromFile);
    }

    private static void AssertLayoutCollection(LifLayoutCollection? schema)
    {
        Assert.NotNull(schema);

        // Check Meta Information
        Assert.Equal("Sample Project", schema.MetaInformation.ProjectIdentification);
        Assert.Equal("Sample Creator", schema.MetaInformation.Creator);
        Assert.Equal("2069-07-21T00:37:33Z", schema.MetaInformation.ExportTimestamp.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ", CultureInfo.InvariantCulture));
        Assert.Equal("1.0.0", schema.MetaInformation.LifVersion);

        // Check Layouts
        Assert.Equal(2, schema.Layouts.Length);

        // First Layout
        var layout1 = schema.Layouts[0];
        Assert.Equal("layout-001", layout1.LayoutId);
        Assert.Equal("Main Layout", layout1.LayoutName);
        Assert.Equal("1.1", layout1.LayoutVersion);
        Assert.Equal("level-001", layout1.LayoutLevelId);
        Assert.Equal("Primary layout for testing.", layout1.LayoutDescription);

        // First Layout Nodes
        Assert.Equal(2, layout1.Nodes.Length);

        var node1 = layout1.Nodes[0];
        Assert.Equal("node-001", node1.NodeId);
        Assert.Equal("Node A", node1.NodeName);
        Assert.Equal("Entrance node.", node1.NodeDescription);
        Assert.Equal("map-001", node1.MapId);
        Assert.Equal(1000.0, node1.NodePosition.X);
        Assert.Equal(1500.0, node1.NodePosition.Y);

        // Node Vehicle Type Properties
        Assert.Equal(2, node1.VehicleTypeNodeProperties.Length);
        var vehicleType1 = node1.VehicleTypeNodeProperties[0];
        Assert.Equal("vehicle-001", vehicleType1.VehicleTypeId);
        Assert.Equal(90.0, vehicleType1.Theta);

        // Actions for Vehicle Type 1
        Assert.NotNull(vehicleType1.Actions);
        Assert.Single(vehicleType1.Actions);
        var action1 = vehicleType1.Actions[0];
        Assert.Equal("move", action1.ActionType);
        Assert.Equal("Move forward", action1.ActionDescription);
        Assert.True(action1.ActionRequired);
        Assert.Equal("HARD", action1.BlockingType);
        Assert.Equal(2, action1.ActionParameters?.Length);
        Assert.Equal("speed", action1.ActionParameters?[0].Key);
        Assert.Equal("fast", action1.ActionParameters?[0].Value);

        // Edges
        Assert.Equal(2, layout1.Edges.Length);
        var edge1 = layout1.Edges[0];
        Assert.Equal("edge-001", edge1.EdgeId);
        Assert.Equal("node-001", edge1.StartNodeId);
        Assert.Equal("node-002", edge1.EndNodeId);

        // Vehicle Type Edge Properties for Edge 1
        Assert.Single(edge1.VehicleTypeEdgeProperties);
        var edgeVehicleType1 = edge1.VehicleTypeEdgeProperties[0];
        Assert.Equal("vehicle-001", edgeVehicleType1.VehicleTypeId);
        Assert.Equal(0.0, edgeVehicleType1.VehicleOrientation);
        Assert.Equal("TANGENTIAL", edgeVehicleType1.OrientationType);
        Assert.True(edgeVehicleType1.RotationAllowed);
        Assert.Equal(1.5, edgeVehicleType1.MaxSpeed);
        Assert.Equal(0.5, edgeVehicleType1.MaxRotationSpeed);
        Assert.True(edgeVehicleType1.LoadRestriction?.Unloaded);
        Assert.False(edgeVehicleType1.LoadRestriction?.Loaded);
        Assert.Equal(["set1", "set2"], edgeVehicleType1.LoadRestriction?.LoadSetNames);

        // Stations
        Assert.Equal(2, layout1.Stations.Length);
        var station1 = layout1.Stations[0];
        Assert.Equal("station-001", station1.StationId);
        Assert.Equal(["node-001", "node-002"], station1.InteractionNodeIds);
        Assert.Equal("Station A", station1.StationName);
        Assert.Equal("Primary loading station.", station1.StationDescription);
        Assert.Equal(1000.0, station1.StationPosition?.X);
        Assert.Equal(1000.0, station1.StationPosition?.Y);
        Assert.Equal(0.0, station1.StationPosition?.Theta);

        // Second Layout
        var layout2 = schema.Layouts[1];
        Assert.Equal("layout-002", layout2.LayoutId);
        Assert.Equal("Secondary Layout", layout2.LayoutName);
        Assert.Equal("1.0", layout2.LayoutVersion);
        Assert.Equal("level-002", layout2.LayoutLevelId);

        // Second Layout Nodes
        Assert.Single(layout2.Nodes);
        var node3 = layout2.Nodes[0];
        Assert.Equal("node-003", node3.NodeId);
        Assert.Equal(3000.0, node3.NodePosition.X);
        Assert.Equal(3500.0, node3.NodePosition.Y);
        Assert.Single(node3.VehicleTypeNodeProperties);
        Assert.Equal("vehicle-003", node3.VehicleTypeNodeProperties[0].VehicleTypeId);
        Assert.Equal(270.0, node3.VehicleTypeNodeProperties[0].Theta);

        // No edges and stations in the second layout
        Assert.Empty(layout2.Edges);
        Assert.NotNull(layout2.Stations);
        Assert.Empty(layout2.Stations);
    }
}