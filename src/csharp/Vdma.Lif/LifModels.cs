// ReSharper disable PropertyCanBeMadeInitOnly.Global
// ReSharper disable ClassNeverInstantiated.Global
// ReSharper disable PartialTypeWithSinglePart
// ReSharper disable UnusedAutoPropertyAccessor.Global
// ReSharper disable UnusedMember.Global

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
    [JsonPropertyName("layouts")]
    public Layout[] Layouts { get; set; }

    /// <summary>
    ///     Contains metadata about the project and the LIF file.
    /// </summary>
    [JsonPropertyName("metaInformation")]
    public MetaInformation MetaInformation { get; set; }
}

public partial class Layout
{
    /// <summary>
    ///     List of edges in the layout. Edges represent paths between nodes.
    /// </summary>
    [JsonPropertyName("edges")]
    public Edge[] Edges { get; set; }

    /// <summary>
    ///     Description of the layout. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutDescription")]
    public string LayoutDescription { get; set; }

    /// <summary>
    ///     Unique identifier for the layout.
    /// </summary>
    [JsonPropertyName("layoutId")]
    public string LayoutId { get; set; }

    /// <summary>
    ///     Unique identifier for the layout level.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutLevelId")]
    public string LayoutLevelId { get; set; }

    /// <summary>
    ///     Name of the layout.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutName")]
    public string LayoutName { get; set; }

    /// <summary>
    ///     Version number of the layout. It is suggested that this be an integer, represented as a
    ///     string, incremented with each change, starting at 1.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("layoutVersion")]
    public string LayoutVersion { get; set; }

    /// <summary>
    ///     List of nodes in the layout. Nodes are locations where vehicles can navigate to.
    /// </summary>
    [JsonPropertyName("nodes")]
    public Node[] Nodes { get; set; }

    /// <summary>
    ///     List of stations in the layout where vehicles perform specific actions.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stations")]
    public Station[] Stations { get; set; }
}

public partial class Edge
{
    /// <summary>
    ///     Unique identifier for the edge.
    /// </summary>
    [JsonPropertyName("edgeId")]
    public string EdgeId { get; set; }

    /// <summary>
    ///     ID of the ending node for this edge.
    /// </summary>
    [JsonPropertyName("endNodeId")]
    public string EndNodeId { get; set; }

    /// <summary>
    ///     ID of the starting node for this edge.
    /// </summary>
    [JsonPropertyName("startNodeId")]
    public string StartNodeId { get; set; }

    /// <summary>
    ///     Vehicle-specific properties for the edge.
    /// </summary>
    [JsonPropertyName("vehicleTypeEdgeProperties")]
    public VehicleTypeEdgeProperty[] VehicleTypeEdgeProperties { get; set; }
}

public partial class VehicleTypeEdgeProperty
{
    /// <summary>
    ///     Load restrictions for this edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("loadRestriction")]
    public LoadRestriction LoadRestriction { get; set; }

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
    public string OrientationType { get; set; }

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
    public string RotationAtEndNodeAllowed { get; set; }

    /// <summary>
    ///     Specifies if rotation is allowed at the start node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("rotationAtStartNodeAllowed")]
    public string RotationAtStartNodeAllowed { get; set; }

    /// <summary>
    ///     Trajectory information for this edge, if applicable. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("trajectory")]
    public Trajectory Trajectory { get; set; }

    /// <summary>
    ///     Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]
    /// </summary>
    [JsonPropertyName("vehicleOrientation")]
    public double VehicleOrientation { get; set; }

    /// <summary>
    ///     Identifier for the vehicle type.
    /// </summary>
    [JsonPropertyName("vehicleTypeId")]
    public string VehicleTypeId { get; set; }
}

/// <summary>
///     Load restrictions for this edge. *Optional*.
/// </summary>
public partial class LoadRestriction
{
    /// <summary>
    ///     Indicates if the edge can be traversed with a load.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("loaded")]
    public bool? Loaded { get; set; }

    /// <summary>
    ///     Names of the load sets allowed on this edge. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("loadSetNames")]
    public string[] LoadSetNames { get; set; }

    /// <summary>
    ///     Indicates if the edge can be traversed without a load.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("unloaded")]
    public bool? Unloaded { get; set; }
}

/// <summary>
///     Trajectory information for this edge, if applicable. *Optional*.
/// </summary>
public partial class Trajectory
{
    /// <summary>
    ///     Control points defining the trajectory. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("controlPoints")]
    public ControlPoint[] ControlPoints { get; set; }

    /// <summary>
    ///     Degree of the trajectory curve. Default is 3. Range: [1 ... 3]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("degree")]
    public long? Degree { get; set; }

    /// <summary>
    ///     Knot vector for the trajectory. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
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
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the control point in meters.
    /// </summary>
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
    public string MapId { get; set; }

    /// <summary>
    ///     Description of the node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("nodeDescription")]
    public string NodeDescription { get; set; }

    /// <summary>
    ///     Unique identifier for the node.
    /// </summary>
    [JsonPropertyName("nodeId")]
    public string NodeId { get; set; }

    /// <summary>
    ///     Name of the node. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("nodeName")]
    public string NodeName { get; set; }

    /// <summary>
    ///     Position of the node on the map (in meters).
    /// </summary>
    [JsonPropertyName("nodePosition")]
    public NodePosition NodePosition { get; set; }

    /// <summary>
    ///     Vehicle-specific properties related to the node.
    /// </summary>
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
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the node in meters. Range: [float64.min... float64.max]
    /// </summary>
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
    public Action[] Actions { get; set; }

    /// <summary>
    ///     Absolute orientation of the vehicle on the node in reference to the global origin’s
    ///     rotation. Range: [-Pi ... Pi]
    /// </summary>
    [JsonPropertyName("theta")]
    public double Theta { get; set; }

    /// <summary>
    ///     Identifier for the vehicle type.
    /// </summary>
    [JsonPropertyName("vehicleTypeId")]
    public string VehicleTypeId { get; set; }
}

public partial class Action
{
    /// <summary>
    ///     Description of the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionDescription")]
    public string ActionDescription { get; set; }

    /// <summary>
    ///     Parameters associated with the action. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionParameters")]
    public ActionParameter[] ActionParameters { get; set; }

    /// <summary>
    ///     Type of action (e.g., move, load, unload).
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("actionType")]
    public string ActionType { get; set; }

    /// <summary>
    ///     Specifies if the action is blocking (HARD or SOFT).
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("blockingType")]
    public string BlockingType { get; set; }

    /// <summary>
    ///     Whether the action is mandatory.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("required")]
    public bool? ActionRequired { get; set; }
}

public partial class ActionParameter
{
    /// <summary>
    ///     Key of the action parameter.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("key")]
    public string Key { get; set; }

    /// <summary>
    ///     Value of the action parameter.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("value")]
    public string Value { get; set; }
}

public partial class Station
{
    /// <summary>
    ///     List of node IDs where the station interacts.
    /// </summary>
    [JsonPropertyName("interactionNodeIds")]
    public string[] InteractionNodeIds { get; set; }

    /// <summary>
    ///     Description of the station. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationDescription")]
    public string StationDescription { get; set; }

    /// <summary>
    ///     Height of the station, if applicable, in meters. *Optional*. Range: [0.0 ... float64.max]
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationHeight")]
    public double? StationHeight { get; set; }

    /// <summary>
    ///     Unique identifier for the station.
    /// </summary>
    [JsonPropertyName("stationId")]
    public string StationId { get; set; }

    /// <summary>
    ///     Name of the station. *Optional*.
    /// </summary>
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
    [JsonPropertyName("stationName")]
    public string StationName { get; set; }

    /// <summary>
    ///     Position of the station on the map (in meters).
    /// </summary>
    [JsonPropertyName("stationPosition")]
    public StationPosition StationPosition { get; set; }
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
    [JsonPropertyName("x")]
    public double X { get; set; }

    /// <summary>
    ///     Y coordinate of the station in meters. Range: [float64.min ... float64.max]
    /// </summary>
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
    [JsonPropertyName("creator")]
    public string Creator { get; set; }

    /// <summary>
    ///     The timestamp at which this LIF file was created/updated/modified. Format is ISO8601 in
    ///     UTC.
    /// </summary>
    [JsonPropertyName("exportTimestamp")]
    public DateTimeOffset ExportTimestamp { get; set; }

    /// <summary>
    ///     Version of the LIF file format. Follows semantic versioning (Major.Minor.Patch).
    /// </summary>
    [JsonPropertyName("lifVersion")]
    public string LifVersion { get; set; }

    /// <summary>
    ///     Human-readable name of the project (e.g., for display purposes).
    /// </summary>
    [JsonPropertyName("projectIdentification")]
    public string ProjectIdentification { get; set; }
}