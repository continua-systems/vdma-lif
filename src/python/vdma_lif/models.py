
from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except BaseException:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


@dataclass
class LoadRestriction:
    """Load restrictions for this edge. *Optional*."""

    loaded: Optional[bool] = None
    """Indicates if the edge can be traversed with a load."""

    load_set_names: Optional[List[str]] = None
    """Names of the load sets allowed on this edge. *Optional*."""

    unloaded: Optional[bool] = None
    """Indicates if the edge can be traversed without a load."""

    @staticmethod
    def from_dict(obj: Any) -> 'LoadRestriction':
        assert isinstance(obj, dict)
        loaded = from_union([from_bool, from_none], obj.get("loaded"))
        load_set_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("loadSetNames"))
        unloaded = from_union([from_bool, from_none], obj.get("unloaded"))
        return LoadRestriction(loaded, load_set_names, unloaded)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.loaded is not None:
            result["loaded"] = from_union([from_bool, from_none], self.loaded)
        if self.load_set_names is not None:
            result["loadSetNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.load_set_names)
        if self.unloaded is not None:
            result["unloaded"] = from_union([from_bool, from_none], self.unloaded)
        return result


@dataclass
class ControlPoint:
    x: float
    """X coordinate of the control point in meters."""

    y: float
    """Y coordinate of the control point in meters."""

    weight: Optional[float] = None
    """The weight with which this control point pulls on the curve. When not defined, the
    default is 1.0. Range: [0.0 ... float64.max]
    """

    @staticmethod
    def from_dict(obj: Any) -> 'ControlPoint':
        assert isinstance(obj, dict)
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        weight = from_union([from_float, from_none], obj.get("weight"))
        return ControlPoint(x, y, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        if self.weight is not None:
            result["weight"] = from_union([to_float, from_none], self.weight)
        return result


@dataclass
class Trajectory:
    """Trajectory information for this edge, if applicable. *Optional*."""

    control_points: Optional[List[ControlPoint]] = None
    """Control points defining the trajectory. *Optional*."""

    degree: Optional[int] = None
    """Degree of the trajectory curve. Default is 3. Range: [1 ... 3]"""

    knot_vector: Optional[List[float]] = None
    """Knot vector for the trajectory. *Optional*."""

    @staticmethod
    def from_dict(obj: Any) -> 'Trajectory':
        assert isinstance(obj, dict)
        control_points = from_union([lambda x: from_list(ControlPoint.from_dict, x),
                                    from_none], obj.get("controlPoints"))
        degree = from_union([from_int, from_none], obj.get("degree"))
        knot_vector = from_union([lambda x: from_list(from_float, x), from_none], obj.get("knotVector"))
        return Trajectory(control_points, degree, knot_vector)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.control_points is not None:
            result["controlPoints"] = from_union([lambda x: from_list(
                lambda x: to_class(ControlPoint, x), x), from_none], self.control_points)
        if self.degree is not None:
            result["degree"] = from_union([from_int, from_none], self.degree)
        if self.knot_vector is not None:
            result["knotVector"] = from_union([lambda x: from_list(to_float, x), from_none], self.knot_vector)
        return result


@dataclass
class VehicleTypeEdgeProperty:
    vehicle_orientation: float
    """Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]"""

    vehicle_type_id: str
    """Identifier for the vehicle type."""

    load_restriction: Optional[LoadRestriction] = None
    """Load restrictions for this edge. *Optional*."""

    max_height: Optional[float] = None
    """Maximum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
    float64.max]
    """
    max_rotation_speed: Optional[float] = None
    """Maximum rotation speed allowed on this edge in radians per second. *Optional*. Range:
    [0.0 ... float64.max]
    """
    max_speed: Optional[float] = None
    """Maximum speed allowed on this edge in meters per second. Range: [0.0 ... float64.max]"""

    min_height: Optional[float] = None
    """Minimum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
    float64.max]
    """
    orientation_type: Optional[str] = None
    """Type of orientation (e.g., TANGENTIAL)."""

    rotation_allowed: Optional[bool] = None
    """Indicates if rotation is allowed while on the edge. *Optional*."""

    rotation_at_end_node_allowed: Optional[str] = None
    """Specifies if rotation is allowed at the end node. *Optional*."""

    rotation_at_start_node_allowed: Optional[str] = None
    """Specifies if rotation is allowed at the start node. *Optional*."""

    trajectory: Optional[Trajectory] = None
    """Trajectory information for this edge, if applicable. *Optional*."""

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeEdgeProperty':
        assert isinstance(obj, dict)
        vehicle_orientation = from_float(obj.get("vehicleOrientation"))
        vehicle_type_id = from_str(obj.get("vehicleTypeId"))
        load_restriction = from_union([LoadRestriction.from_dict, from_none], obj.get("loadRestriction"))
        max_height = from_union([from_float, from_none], obj.get("maxHeight"))
        max_rotation_speed = from_union([from_float, from_none], obj.get("maxRotationSpeed"))
        max_speed = from_union([from_float, from_none], obj.get("maxSpeed"))
        min_height = from_union([from_float, from_none], obj.get("minHeight"))
        orientation_type = from_union([from_str, from_none], obj.get("orientationType"))
        rotation_allowed = from_union([from_bool, from_none], obj.get("rotationAllowed"))
        rotation_at_end_node_allowed = from_union([from_str, from_none], obj.get("rotationAtEndNodeAllowed"))
        rotation_at_start_node_allowed = from_union([from_str, from_none], obj.get("rotationAtStartNodeAllowed"))
        trajectory = from_union([Trajectory.from_dict, from_none], obj.get("trajectory"))
        return VehicleTypeEdgeProperty(vehicle_orientation, vehicle_type_id, load_restriction, max_height, max_rotation_speed, max_speed,
                                       min_height, orientation_type, rotation_allowed, rotation_at_end_node_allowed, rotation_at_start_node_allowed, trajectory)

    def to_dict(self) -> dict:
        result: dict = {}
        result["vehicleOrientation"] = to_float(self.vehicle_orientation)
        result["vehicleTypeId"] = from_str(self.vehicle_type_id)
        if self.load_restriction is not None:
            result["loadRestriction"] = from_union(
                [lambda x: to_class(LoadRestriction, x), from_none], self.load_restriction)
        if self.max_height is not None:
            result["maxHeight"] = from_union([to_float, from_none], self.max_height)
        if self.max_rotation_speed is not None:
            result["maxRotationSpeed"] = from_union([to_float, from_none], self.max_rotation_speed)
        if self.max_speed is not None:
            result["maxSpeed"] = from_union([to_float, from_none], self.max_speed)
        if self.min_height is not None:
            result["minHeight"] = from_union([to_float, from_none], self.min_height)
        if self.orientation_type is not None:
            result["orientationType"] = from_union([from_str, from_none], self.orientation_type)
        if self.rotation_allowed is not None:
            result["rotationAllowed"] = from_union([from_bool, from_none], self.rotation_allowed)
        if self.rotation_at_end_node_allowed is not None:
            result["rotationAtEndNodeAllowed"] = from_union([from_str, from_none], self.rotation_at_end_node_allowed)
        if self.rotation_at_start_node_allowed is not None:
            result["rotationAtStartNodeAllowed"] = from_union(
                [from_str, from_none], self.rotation_at_start_node_allowed)
        if self.trajectory is not None:
            result["trajectory"] = from_union([lambda x: to_class(Trajectory, x), from_none], self.trajectory)
        return result


@dataclass
class Edge:
    edge_id: str
    """Unique identifier for the edge."""

    end_node_id: str
    """ID of the ending node for this edge."""

    start_node_id: str
    """ID of the starting node for this edge."""

    vehicle_type_edge_properties: List[VehicleTypeEdgeProperty]
    """Vehicle-specific properties for the edge."""

    @staticmethod
    def from_dict(obj: Any) -> 'Edge':
        assert isinstance(obj, dict)
        edge_id = from_str(obj.get("edgeId"))
        end_node_id = from_str(obj.get("endNodeId"))
        start_node_id = from_str(obj.get("startNodeId"))
        vehicle_type_edge_properties = from_list(
            VehicleTypeEdgeProperty.from_dict,
            obj.get("vehicleTypeEdgeProperties"))
        return Edge(edge_id, end_node_id, start_node_id, vehicle_type_edge_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["edgeId"] = from_str(self.edge_id)
        result["endNodeId"] = from_str(self.end_node_id)
        result["startNodeId"] = from_str(self.start_node_id)
        result["vehicleTypeEdgeProperties"] = from_list(lambda x: to_class(
            VehicleTypeEdgeProperty, x), self.vehicle_type_edge_properties)
        return result


@dataclass
class NodePosition:
    """Position of the node on the map (in meters)."""

    x: float
    """X coordinate of the node in meters. Range: [float64.min ... float64.max]"""

    y: float
    """Y coordinate of the node in meters. Range: [float64.min... float64.max]"""

    @staticmethod
    def from_dict(obj: Any) -> 'NodePosition':
        assert isinstance(obj, dict)
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        return NodePosition(x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        return result


@dataclass
class ActionParameter:
    key: Optional[str] = None
    """Key of the action parameter."""

    value: Optional[str] = None
    """Value of the action parameter."""

    @staticmethod
    def from_dict(obj: Any) -> 'ActionParameter':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("key"))
        value = from_union([from_str, from_none], obj.get("value"))
        return ActionParameter(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.key is not None:
            result["key"] = from_union([from_str, from_none], self.key)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class Action:
    action_description: Optional[str] = None
    """Description of the action. *Optional*."""

    action_parameters: Optional[List[ActionParameter]] = None
    """Parameters associated with the action. *Optional*."""

    action_type: Optional[str] = None
    """Type of action (e.g., move, load, unload)."""

    blocking_type: Optional[str] = None
    """Specifies if the action is blocking (HARD or SOFT)."""

    required: Optional[bool] = None
    """Whether the action is mandatory."""

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        action_description = from_union([from_str, from_none], obj.get("actionDescription"))
        action_parameters = from_union([lambda x: from_list(ActionParameter.from_dict, x),
                                       from_none], obj.get("actionParameters"))
        action_type = from_union([from_str, from_none], obj.get("actionType"))
        blocking_type = from_union([from_str, from_none], obj.get("blockingType"))
        required = from_union([from_bool, from_none], obj.get("required"))
        return Action(action_description, action_parameters, action_type, blocking_type, required)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.action_description is not None:
            result["actionDescription"] = from_union([from_str, from_none], self.action_description)
        if self.action_parameters is not None:
            result["actionParameters"] = from_union([lambda x: from_list(
                lambda x: to_class(ActionParameter, x), x), from_none], self.action_parameters)
        if self.action_type is not None:
            result["actionType"] = from_union([from_str, from_none], self.action_type)
        if self.blocking_type is not None:
            result["blockingType"] = from_union([from_str, from_none], self.blocking_type)
        if self.required is not None:
            result["required"] = from_union([from_bool, from_none], self.required)
        return result


@dataclass
class VehicleTypeNodeProperty:
    vehicle_type_id: str
    """Identifier for the vehicle type."""

    actions: Optional[List[Action]] = None
    """List of actions that the vehicle can perform at the node. *Optional*."""

    theta: Optional[float] = None
    """Absolute orientation of the vehicle on the node in reference to the global origin’s
    rotation. Range: [-Pi ... Pi]
    """

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeNodeProperty':
        assert isinstance(obj, dict)
        vehicle_type_id = from_str(obj.get("vehicleTypeId"))
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        theta = from_union([from_float, from_none], obj.get("theta"))
        return VehicleTypeNodeProperty(vehicle_type_id, actions, theta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["vehicleTypeId"] = from_str(self.vehicle_type_id)
        if self.actions is not None:
            result["actions"] = from_union([lambda x: from_list(
                lambda x: to_class(Action, x), x), from_none], self.actions)
        if self.theta is not None:
            result["theta"] = from_union([to_float, from_none], self.theta)
        return result


@dataclass
class Node:
    node_id: str
    """Unique identifier for the node."""

    node_position: NodePosition
    """Position of the node on the map (in meters)."""

    vehicle_type_node_properties: List[VehicleTypeNodeProperty]
    """Vehicle-specific properties related to the node."""

    map_id: Optional[str] = None
    """Identifier for the map that this node belongs to. *Optional*."""

    node_description: Optional[str] = None
    """Description of the node. *Optional*."""

    node_name: Optional[str] = None
    """Name of the node. *Optional*."""

    @staticmethod
    def from_dict(obj: Any) -> 'Node':
        assert isinstance(obj, dict)
        node_id = from_str(obj.get("nodeId"))
        node_position = NodePosition.from_dict(obj.get("nodePosition"))
        vehicle_type_node_properties = from_list(
            VehicleTypeNodeProperty.from_dict,
            obj.get("vehicleTypeNodeProperties"))
        map_id = from_union([from_str, from_none], obj.get("mapId"))
        node_description = from_union([from_str, from_none], obj.get("nodeDescription"))
        node_name = from_union([from_str, from_none], obj.get("nodeName"))
        return Node(node_id, node_position, vehicle_type_node_properties, map_id, node_description, node_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nodeId"] = from_str(self.node_id)
        result["nodePosition"] = to_class(NodePosition, self.node_position)
        result["vehicleTypeNodeProperties"] = from_list(lambda x: to_class(
            VehicleTypeNodeProperty, x), self.vehicle_type_node_properties)
        if self.map_id is not None:
            result["mapId"] = from_union([from_str, from_none], self.map_id)
        if self.node_description is not None:
            result["nodeDescription"] = from_union([from_str, from_none], self.node_description)
        if self.node_name is not None:
            result["nodeName"] = from_union([from_str, from_none], self.node_name)
        return result


@dataclass
class StationPosition:
    """Position of the station on the map (in meters)."""

    x: float
    """X coordinate of the station in meters. Range: [float64.min ... float64.max]"""

    y: float
    """Y coordinate of the station in meters. Range: [float64.min ... float64.max]"""

    theta: Optional[float] = None
    """Orientation of the station. Unit: radians. Range: [-Pi ... Pi]"""

    @staticmethod
    def from_dict(obj: Any) -> 'StationPosition':
        assert isinstance(obj, dict)
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        theta = from_union([from_float, from_none], obj.get("theta"))
        return StationPosition(x, y, theta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        if self.theta is not None:
            result["theta"] = from_union([to_float, from_none], self.theta)
        return result


@dataclass
class Station:
    interaction_node_ids: List[str]
    """List of node IDs where the station interacts."""

    station_id: str
    """Unique identifier for the station."""

    station_position: StationPosition
    """Position of the station on the map (in meters)."""

    station_description: Optional[str] = None
    """Description of the station. *Optional*."""

    station_height: Optional[float] = None
    """Height of the station, if applicable, in meters. *Optional*. Range: [0.0 ... float64.max]"""

    station_name: Optional[str] = None
    """Name of the station. *Optional*."""

    @staticmethod
    def from_dict(obj: Any) -> 'Station':
        assert isinstance(obj, dict)
        interaction_node_ids = from_list(from_str, obj.get("interactionNodeIds"))
        station_id = from_str(obj.get("stationId"))
        station_position = StationPosition.from_dict(obj.get("stationPosition"))
        station_description = from_union([from_str, from_none], obj.get("stationDescription"))
        station_height = from_union([from_float, from_none], obj.get("stationHeight"))
        station_name = from_union([from_str, from_none], obj.get("stationName"))
        return Station(interaction_node_ids, station_id, station_position,
                       station_description, station_height, station_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["interactionNodeIds"] = from_list(from_str, self.interaction_node_ids)
        result["stationId"] = from_str(self.station_id)
        result["stationPosition"] = to_class(StationPosition, self.station_position)
        if self.station_description is not None:
            result["stationDescription"] = from_union([from_str, from_none], self.station_description)
        if self.station_height is not None:
            result["stationHeight"] = from_union([to_float, from_none], self.station_height)
        if self.station_name is not None:
            result["stationName"] = from_union([from_str, from_none], self.station_name)
        return result


@dataclass
class Layout:
    edges: List[Edge]
    """List of edges in the layout. Edges represent paths between nodes."""

    layout_id: str
    """Unique identifier for the layout."""

    nodes: List[Node]
    """List of nodes in the layout. Nodes are locations where vehicles can navigate to."""

    layout_description: Optional[str] = None
    """Description of the layout. *Optional*."""

    layout_level_id: Optional[str] = None
    """Unique identifier for the layout level."""

    layout_name: Optional[str] = None
    """Name of the layout."""

    layout_version: Optional[str] = None
    """Version number of the layout. It is suggested that this be an integer, represented as a
    string, incremented with each change, starting at 1.
    """
    stations: Optional[List[Station]] = None
    """List of stations in the layout where vehicles perform specific actions."""

    @staticmethod
    def from_dict(obj: Any) -> 'Layout':
        assert isinstance(obj, dict)
        edges = from_list(Edge.from_dict, obj.get("edges"))
        layout_id = from_str(obj.get("layoutId"))
        nodes = from_list(Node.from_dict, obj.get("nodes"))
        layout_description = from_union([from_str, from_none], obj.get("layoutDescription"))
        layout_level_id = from_union([from_str, from_none], obj.get("layoutLevelId"))
        layout_name = from_union([from_str, from_none], obj.get("layoutName"))
        layout_version = from_union([from_str, from_none], obj.get("layoutVersion"))
        stations = from_union([lambda x: from_list(Station.from_dict, x), from_none], obj.get("stations"))
        return Layout(edges, layout_id, nodes, layout_description,
                      layout_level_id, layout_name, layout_version, stations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["edges"] = from_list(lambda x: to_class(Edge, x), self.edges)
        result["layoutId"] = from_str(self.layout_id)
        result["nodes"] = from_list(lambda x: to_class(Node, x), self.nodes)
        if self.layout_description is not None:
            result["layoutDescription"] = from_union([from_str, from_none], self.layout_description)
        if self.layout_level_id is not None:
            result["layoutLevelId"] = from_union([from_str, from_none], self.layout_level_id)
        if self.layout_name is not None:
            result["layoutName"] = from_union([from_str, from_none], self.layout_name)
        if self.layout_version is not None:
            result["layoutVersion"] = from_union([from_str, from_none], self.layout_version)
        if self.stations is not None:
            result["stations"] = from_union([lambda x: from_list(
                lambda x: to_class(Station, x), x), from_none], self.stations)
        return result


@dataclass
class MetaInformation:
    """Contains metadata about the project and the LIF file."""

    creator: str
    """Creator of the LIF file (e.g., name of company or person)."""

    export_timestamp: datetime
    """The timestamp at which this LIF file was created/updated/modified. Format is ISO8601 in
    UTC.
    """
    lif_version: str
    """Version of the LIF file format. Follows semantic versioning (Major.Minor.Patch)."""

    project_identification: str
    """Human-readable name of the project (e.g., for display purposes)."""

    @staticmethod
    def from_dict(obj: Any) -> 'MetaInformation':
        assert isinstance(obj, dict)
        creator = from_str(obj.get("creator"))
        export_timestamp = from_datetime(obj.get("exportTimestamp"))
        lif_version = from_str(obj.get("lifVersion"))
        project_identification = from_str(obj.get("projectIdentification"))
        return MetaInformation(creator, export_timestamp, lif_version, project_identification)

    def to_dict(self) -> dict:
        result: dict = {}
        result["creator"] = from_str(self.creator)
        result["exportTimestamp"] = self.export_timestamp.isoformat()
        result["lifVersion"] = from_str(self.lif_version)
        result["projectIdentification"] = from_str(self.project_identification)
        return result


@dataclass
class LIFLayoutCollection:
    layouts: List[Layout]
    """Collection of layouts used in the facility by the driverless transport system. All
    layouts refer to the same global origin.
    """
    meta_information: MetaInformation
    """Contains metadata about the project and the LIF file."""

    @staticmethod
    def from_dict(obj: Any) -> 'LIFLayoutCollection':
        assert isinstance(obj, dict)
        layouts = from_list(Layout.from_dict, obj.get("layouts"))
        meta_information = MetaInformation.from_dict(obj.get("metaInformation"))
        return LIFLayoutCollection(layouts, meta_information)

    def to_dict(self) -> dict:
        result: dict = {}
        result["layouts"] = from_list(lambda x: to_class(Layout, x), self.layouts)
        result["metaInformation"] = to_class(MetaInformation, self.meta_information)
        return result


def lif_layout_collection_from_dict(s: Any) -> LIFLayoutCollection:
    return LIFLayoutCollection.from_dict(s)


def lif_layout_collection_to_dict(x: LIFLayoutCollection) -> Any:
    return to_class(LIFLayoutCollection, x)
