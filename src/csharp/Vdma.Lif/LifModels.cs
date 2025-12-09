// ReSharper disable PropertyCanBeMadeInitOnly.Global
// ReSharper disable ClassNeverInstantiated.Global
// ReSharper disable PartialTypeWithSinglePart
// ReSharper disable UnusedAutoPropertyAccessor.Global
// ReSharper disable UnusedMember.Global

using System.Globalization;
using System.Text.Json;
using System.Text.Json.Serialization;

#pragma warning disable CS8618
#pragma warning disable CS8601
#pragma warning disable CS8603

namespace Vdma.Lif;

public partial class LifLayoutCollection
{
    /// <summary>
    ///     Collection of layouts used in the facility by the driverless transport system. All
    ///     layouts refer to the same global origin.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("layouts")]
    public Layout[] Layouts { get; set; }

    /// <summary>
    ///     Contains metadata about the project and the LIF file.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("metaInformation")]
    public MetaInformation MetaInformation { get; set; }
}

public partial class Layout
{
    /// <summary>
    ///     List of edges in the layout. Edges represent paths between nodes.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("edges")]
    public Edge[] Edges { get; set; }

    /// <summary>
    ///     Description of the layout. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutDescription")]
    public string? LayoutDescription { get; set; }

    /// <summary>
    ///     Unique identifier for the layout.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("layoutId")]
    public string LayoutId { get; set; }

    /// <summary>
    ///     Unique identifier for the layout level.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutLevelId")]
    public string? LayoutLevelId { get; set; }

    /// <summary>
    ///     Name of the layout.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutName")]
    public string? LayoutName { get; set; }

    /// <summary>
    ///     Version number of the layout. It is suggested that this be an integer, represented as a
    ///     string, incremented with each change, starting at 1.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("layoutVersion")]
    public string LayoutVersion { get; set; }

    /// <summary>
    ///     List of nodes in the layout. Nodes are locations where vehicles can navigate to.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("nodes")]
    public Node[] Nodes { get; set; }

    /// <summary>
    ///     List of stations in the layout where vehicles perform specific actions.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("stations")]
    public Station[] Stations { get; set; }
}

public partial class Edge
{
    /// <summary>
    ///     Unique identifier for the edge.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("edgeId")]
    public string EdgeId { get; set; }

    /// <summary>
    ///     ID of the ending node for this edge.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("endNodeId")]
    public string EndNodeId { get; set; }

    /// <summary>
    ///     ID of the starting node for this edge.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("startNodeId")]
    public string StartNodeId { get; set; }

    /// <summary>
    ///     Vehicle-specific properties for the edge.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("vehicleTypeEdgeProperties")]
    public VehicleTypeEdgeProperty[] VehicleTypeEdgeProperties { get; set; }
}

public partial class VehicleTypeEdgeProperty
{
    /// <summary>
    ///     Actions that can be integrated into the order by the (third-party) master control system
    ///     each time any vehicle with the corresponding vehicleTypeId is sent an order/order update
    ///     that contains this edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actions")]
    public VehicleTypeEdgePropertyAction[]? Actions { get; set; }

    /// <summary>
    ///     Load restrictions for this edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("loadRestriction")]
    public LoadRestriction? LoadRestriction { get; set; }

    /// <summary>
    ///     Maximum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
    ///     float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("maxHeight")]
    public double? MaxHeight { get; set; }

    /// <summary>
    ///     Maximum rotation speed allowed on this edge in radians per second. *Optional*. Range:
    ///     [0.0 ... float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("maxRotationSpeed")]
    public double? MaxRotationSpeed { get; set; }

    /// <summary>
    ///     Maximum speed allowed on this edge in meters per second. Range: [0.0 ... float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("maxSpeed")]
    public double? MaxSpeed { get; set; }

    /// <summary>
    ///     Minimum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
    ///     float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("minHeight")]
    public double? MinHeight { get; set; }

    /// <summary>
    ///     Type of orientation (e.g., TANGENTIAL).
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("orientationType")]
    public string? OrientationType { get; set; }

    /// <summary>
    ///     true: Vehicles of the corresponding vehicleTypeId are allowed to enter into automatic
    ///     management by the (third-party) master control system while on this edge. false: Vehicles
    ///     are not allowed to enter into automatic management while on this edge. Default is true if
    ///     not defined.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("reentryAllowed")]
    public bool? ReentryAllowed { get; set; }

    /// <summary>
    ///     Indicates if rotation is allowed while on the edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("rotationAllowed")]
    public bool? RotationAllowed { get; set; }

    /// <summary>
    ///     Specifies if rotation is allowed at the end node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("rotationAtEndNodeAllowed")]
    public string? RotationAtEndNodeAllowed { get; set; }

    /// <summary>
    ///     Specifies if rotation is allowed at the start node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("rotationAtStartNodeAllowed")]
    public string? RotationAtStartNodeAllowed { get; set; }

    /// <summary>
    ///     Trajectory information for this edge, if applicable. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("trajectory")]
    public Trajectory? Trajectory { get; set; }

    /// <summary>
    ///     Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("vehicleOrientation")]
    public double? VehicleOrientation { get; set; }

    /// <summary>
    ///     Identifier for the vehicle type.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("vehicleTypeId")]
    public string VehicleTypeId { get; set; }
}

public partial class VehicleTypeEdgePropertyAction
{
    /// <summary>
    ///     Description of the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionDescription")]
    public string? ActionDescription { get; set; }

    /// <summary>
    ///     Parameters associated with the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionParameters")]
    public PurpleActionParameter[]? ActionParameters { get; set; }

    /// <summary>
    ///     Type of action (e.g., move, load, unload).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("actionType")]
    public string ActionType { get; set; }

    /// <summary>
    ///     Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
    ///     other actions, but not moving. HARD: is the only allowed action at this time.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("blockingType")]
    public BlockingType BlockingType { get; set; }

    /// <summary>
    ///     Defines if the action is required. REQUIRED: The (third-party) master control system must
    ///     always communicate this action. CONDITIONAL: The action may or may not be required
    ///     contingent upon various factors. OPTIONAL: The action may or may not be communicated at
    ///     the master control system's discretion.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("requirementType")]
    public RequirementType? RequirementType { get; set; }
}

public partial class PurpleActionParameter
{
    /// <summary>
    ///     Key of the action parameter.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("key")]
    public string Key { get; set; }

    /// <summary>
    ///     Value of the action parameter.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("value")]
    public string Value { get; set; }
}

/// <summary>
///     Load restrictions for this edge. *Optional*.
/// </summary>
public partial class LoadRestriction
{
    /// <summary>
    ///     Indicates if the edge can be traversed with a load.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("loaded")]
    public bool Loaded { get; set; }

    /// <summary>
    ///     Names of the load sets allowed on this edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("loadSetNames")]
    public string[]? LoadSetNames { get; set; }

    /// <summary>
    ///     Indicates if the edge can be traversed without a load.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("unloaded")]
    public bool Unloaded { get; set; }
}

/// <summary>
///     Trajectory information for this edge, if applicable. *Optional*.
/// </summary>
public partial class Trajectory
{
    /// <summary>
    ///     Control points defining the trajectory.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("controlPoints")]
    public ControlPoint[] ControlPoints { get; set; }

    /// <summary>
    ///     Degree of the trajectory curve. Default is 3. Range: [1 ... 3]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("degree")]
    public long? Degree { get; set; }

    /// <summary>
    ///     Knot vector for the trajectory.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("knotVector")]
    public double[] KnotVector { get; set; }
}

public partial class ControlPoint
{
    /// <summary>
    ///     The weight with which this control point pulls on the curve. When not defined, the
    ///     default is 1.0. Range: [0.0 ... float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("weight")]
    public double? Weight { get; set; }

    /// <summary>
    ///     X coordinate of the control point in meters.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the control point in meters.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("y")]
    public double Y { get; set; }
}

public partial class Node
{
    /// <summary>
    ///     Identifier for the map that this node belongs to. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("mapId")]
    public string? MapId { get; set; }

    /// <summary>
    ///     Description of the node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("nodeDescription")]
    public string? NodeDescription { get; set; }

    /// <summary>
    ///     Unique identifier for the node.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("nodeId")]
    public string NodeId { get; set; }

    /// <summary>
    ///     Name of the node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("nodeName")]
    public string? NodeName { get; set; }

    /// <summary>
    ///     Position of the node on the map (in meters).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("nodePosition")]
    public NodePosition NodePosition { get; set; }

    /// <summary>
    ///     Vehicle-specific properties related to the node.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("vehicleTypeNodeProperties")]
    public VehicleTypeNodeProperty[] VehicleTypeNodeProperties { get; set; }
}

/// <summary>
///     Position of the node on the map (in meters).
/// </summary>
public partial class NodePosition
{
    /// <summary>
    ///     X coordinate of the node in meters. Range: [float64.min ... float64.max]
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the node in meters. Range: [float64.min... float64.max]
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("y")]
    public double Y { get; set; }
}

public partial class VehicleTypeNodeProperty
{
    /// <summary>
    ///     List of actions that the vehicle can perform at the node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actions")]
    public VehicleTypeNodePropertyAction[]? Actions { get; set; }

    /// <summary>
    ///     Absolute orientation of the vehicle on the node in reference to the global origin’s
    ///     rotation. Range: [-Pi ... Pi]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("theta")]
    public double? Theta { get; set; }

    /// <summary>
    ///     Identifier for the vehicle type.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("vehicleTypeId")]
    public string VehicleTypeId { get; set; }
}

public partial class VehicleTypeNodePropertyAction
{
    /// <summary>
    ///     Description of the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionDescription")]
    public string? ActionDescription { get; set; }

    /// <summary>
    ///     Parameters associated with the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionParameters")]
    public FluffyActionParameter[]? ActionParameters { get; set; }

    /// <summary>
    ///     Type of action (e.g., move, load, unload).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("actionType")]
    public string ActionType { get; set; }

    /// <summary>
    ///     Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
    ///     other actions, but not moving. HARD: is the only allowed action at this time.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("blockingType")]
    public BlockingType BlockingType { get; set; }

    /// <summary>
    ///     Defines if the action is required. REQUIRED: The (third-party) master control system must
    ///     always communicate this action. CONDITIONAL: The action may or may not be required
    ///     contingent upon various factors. OPTIONAL: The action may or may not be communicated at
    ///     the master control system's discretion.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("requirementType")]
    public RequirementType? RequirementType { get; set; }
}

public partial class FluffyActionParameter
{
    /// <summary>
    ///     Key of the action parameter.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("key")]
    public string Key { get; set; }

    /// <summary>
    ///     Value of the action parameter.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("value")]
    public string Value { get; set; }
}

public partial class Station
{
    /// <summary>
    ///     List of node IDs where the station interacts.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("interactionNodeIds")]
    public string[] InteractionNodeIds { get; set; }

    /// <summary>
    ///     Description of the station. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationDescription")]
    public string? StationDescription { get; set; }

    /// <summary>
    ///     Height of the station, if applicable, in meters. *Optional*. Range: [0.0 ... float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationHeight")]
    public double? StationHeight { get; set; }

    /// <summary>
    ///     Unique identifier for the station.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("stationId")]
    public string StationId { get; set; }

    /// <summary>
    ///     Name of the station. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationName")]
    public string? StationName { get; set; }

    /// <summary>
    ///     Position of the station on the map (in meters).
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationPosition")]
    public StationPosition? StationPosition { get; set; }
}

/// <summary>
///     Position of the station on the map (in meters).
/// </summary>
public partial class StationPosition
{
    /// <summary>
    ///     Orientation of the station. Unit: radians. Range: [-Pi ... Pi]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("theta")]
    public double? Theta { get; set; }

    /// <summary>
    ///     X coordinate of the station in meters. Range: [float64.min ... float64.max]
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the station in meters. Range: [float64.min ... float64.max]
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("y")]
    public double Y { get; set; }
}

/// <summary>
///     Contains metadata about the project and the LIF file.
/// </summary>
public partial class MetaInformation
{
    /// <summary>
    ///     Creator of the LIF file (e.g., name of company or person).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("creator")]
    public string Creator { get; set; }

    /// <summary>
    ///     The timestamp at which this LIF file was created/updated/modified. Format is ISO8601 in
    ///     UTC.
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("exportTimestamp")]
    public DateTimeOffset ExportTimestamp { get; set; }

    /// <summary>
    ///     Version of the LIF file format. Follows semantic versioning (Major.Minor.Patch).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("lifVersion")]
    public string LifVersion { get; set; }

    /// <summary>
    ///     Human-readable name of the project (e.g., for display purposes).
    /// </summary>
    [JsonRequired]
    [JsonPropertyName("projectIdentification")]
    public string ProjectIdentification { get; set; }
}

/// <summary>
///     Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
///     other actions, but not moving. HARD: is the only allowed action at this time.
/// </summary>
public enum BlockingType
{
    Hard,
    None,
    Soft
}

/// <summary>
///     Defines if the action is required. REQUIRED: The (third-party) master control system must
///     always communicate this action. CONDITIONAL: The action may or may not be required
///     contingent upon various factors. OPTIONAL: The action may or may not be communicated at
///     the master control system's discretion.
/// </summary>
public enum RequirementType
{
    Conditional,
    Optional,
    Required
}

internal static class Converter
{
    public static readonly JsonSerializerOptions Settings = new(JsonSerializerDefaults.General)
    {
        Converters =
        {
            BlockingTypeConverter.Singleton,
            RequirementTypeConverter.Singleton,
            new DateOnlyConverter(),
            new TimeOnlyConverter(),
            IsoDateTimeOffsetConverter.Singleton
        }
    };
}

internal class BlockingTypeConverter : JsonConverter<BlockingType>
{
    public static readonly BlockingTypeConverter Singleton = new();

    public override bool CanConvert(Type t)
    {
        return t == typeof(BlockingType);
    }

    public override BlockingType Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        switch (value)
        {
            case "HARD":
                return BlockingType.Hard;

            case "NONE":
                return BlockingType.None;

            case "SOFT":
                return BlockingType.Soft;
        }
        throw new Exception("Cannot unmarshal type BlockingType");
    }

    public override void Write(Utf8JsonWriter writer, BlockingType value, JsonSerializerOptions options)
    {
        switch (value)
        {
            case BlockingType.Hard:
                JsonSerializer.Serialize(writer, "HARD", options);
                return;

            case BlockingType.None:
                JsonSerializer.Serialize(writer, "NONE", options);
                return;

            case BlockingType.Soft:
                JsonSerializer.Serialize(writer, "SOFT", options);
                return;
        }
        throw new Exception("Cannot marshal type BlockingType");
    }
}

internal class RequirementTypeConverter : JsonConverter<RequirementType>
{
    public static readonly RequirementTypeConverter Singleton = new();

    public override bool CanConvert(Type t)
    {
        return t == typeof(RequirementType);
    }

    public override RequirementType Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        switch (value)
        {
            case "CONDITIONAL":
                return RequirementType.Conditional;

            case "OPTIONAL":
                return RequirementType.Optional;

            case "REQUIRED":
                return RequirementType.Required;
        }
        throw new Exception("Cannot unmarshal type RequirementType");
    }

    public override void Write(Utf8JsonWriter writer, RequirementType value, JsonSerializerOptions options)
    {
        switch (value)
        {
            case RequirementType.Conditional:
                JsonSerializer.Serialize(writer, "CONDITIONAL", options);
                return;

            case RequirementType.Optional:
                JsonSerializer.Serialize(writer, "OPTIONAL", options);
                return;

            case RequirementType.Required:
                JsonSerializer.Serialize(writer, "REQUIRED", options);
                return;
        }
        throw new Exception("Cannot marshal type RequirementType");
    }
}

public class DateOnlyConverter : JsonConverter<DateOnly>
{
    private readonly string serializationFormat;

    public DateOnlyConverter() : this(null)
    {
    }

    public DateOnlyConverter(string? serializationFormat)
    {
        this.serializationFormat = serializationFormat ?? "yyyy-MM-dd";
    }

    public override DateOnly Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        return DateOnly.Parse(value!);
    }

    public override void Write(Utf8JsonWriter writer, DateOnly value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(value.ToString(serializationFormat));
    }
}

public class TimeOnlyConverter : JsonConverter<TimeOnly>
{
    private readonly string serializationFormat;

    public TimeOnlyConverter() : this(null)
    {
    }

    public TimeOnlyConverter(string? serializationFormat)
    {
        this.serializationFormat = serializationFormat ?? "HH:mm:ss.fff";
    }

    public override TimeOnly Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        return TimeOnly.Parse(value!);
    }

    public override void Write(Utf8JsonWriter writer, TimeOnly value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(value.ToString(serializationFormat));
    }
}

internal class IsoDateTimeOffsetConverter : JsonConverter<DateTimeOffset>
{
    private const string DefaultDateTimeFormat = "yyyy'-'MM'-'dd'T'HH':'mm':'ss.FFFFFFFK";

    public static readonly IsoDateTimeOffsetConverter Singleton = new();
    private CultureInfo? _culture;
    private string? _dateTimeFormat;

    public DateTimeStyles DateTimeStyles { get; set; } = DateTimeStyles.RoundtripKind;

    public string? DateTimeFormat
    {
        get => _dateTimeFormat ?? string.Empty;
        set => _dateTimeFormat = string.IsNullOrEmpty(value) ? null : value;
    }

    public CultureInfo Culture
    {
        get => _culture ?? CultureInfo.CurrentCulture;
        set => _culture = value;
    }

    public override bool CanConvert(Type t)
    {
        return t == typeof(DateTimeOffset);
    }

    public override void Write(Utf8JsonWriter writer, DateTimeOffset value, JsonSerializerOptions options)
    {
        string text;

        if ((DateTimeStyles & DateTimeStyles.AdjustToUniversal) == DateTimeStyles.AdjustToUniversal
            || (DateTimeStyles & DateTimeStyles.AssumeUniversal) == DateTimeStyles.AssumeUniversal)
        {
            value = value.ToUniversalTime();
        }

        text = value.ToString(_dateTimeFormat ?? DefaultDateTimeFormat, Culture);

        writer.WriteStringValue(text);
    }

    public override DateTimeOffset Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var dateText = reader.GetString();

        if (string.IsNullOrEmpty(dateText) == false)
        {
            if (!string.IsNullOrEmpty(_dateTimeFormat))
            {
                return DateTimeOffset.ParseExact(dateText, _dateTimeFormat, Culture, DateTimeStyles);
            }
            return DateTimeOffset.Parse(dateText, Culture, DateTimeStyles);
        }
        return default;
    }
}