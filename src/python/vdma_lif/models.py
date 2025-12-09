
from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


@dataclass
class PurpleActionParameter:
    key: str
    """Key of the action parameter."""

    value: str
    """Value of the action parameter."""

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleActionParameter':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        value = from_str(obj.get("value"))
        return PurpleActionParameter(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["value"] = from_str(self.value)
        return result


class BlockingType(Enum):
    """Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
    other actions, but not moving. HARD: is the only allowed action at this time.
    """
    HARD = "HARD"
    NONE = "NONE"
    SOFT = "SOFT"


class RequirementType(Enum):
    """Defines if the action is required. REQUIRED: The (third-party) master control system must
    always communicate this action. CONDITIONAL: The action may or may not be required
    contingent upon various factors. OPTIONAL: The action may or may not be communicated at
    the master control system's discretion.
    """
    CONDITIONAL = "CONDITIONAL"
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"


@dataclass
class VehicleTypeEdgePropertyAction:
    action_type: str
    """Type of action (e.g., move, load, unload)."""

    blocking_type: BlockingType
    """Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
    other actions, but not moving. HARD: is the only allowed action at this time.
    """
    action_description: Optional[str] = None
    """Description of the action. *Optional*."""

    action_parameters: Optional[List[PurpleActionParameter]] = None
    """Parameters associated with the action. *Optional*."""

    requirement_type: Optional[RequirementType] = None
    """Defines if the action is required. REQUIRED: The (third-party) master control system must
    always communicate this action. CONDITIONAL: The action may or may not be required
    contingent upon various factors. OPTIONAL: The action may or may not be communicated at
    the master control system's discretion.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeEdgePropertyAction':
        assert isinstance(obj, dict)
        action_type = from_str(obj.get("actionType"))
        blocking_type = BlockingType(obj.get("blockingType"))
        action_description = from_union([from_str, from_none], obj.get("actionDescription"))
        action_parameters = from_union([lambda x: from_list(
            PurpleActionParameter.from_dict, x), from_none], obj.get("actionParameters"))
        requirement_type = from_union([RequirementType, from_none], obj.get("requirementType"))
        return VehicleTypeEdgePropertyAction(action_type, blocking_type,
                                             action_description, action_parameters, requirement_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actionType"] = from_str(self.action_type)
        result["blockingType"] = to_enum(BlockingType, self.blocking_type)
        if self.action_description is not None:
            result["actionDescription"] = from_union([from_str, from_none], self.action_description)
        if self.action_parameters is not None:
            result["actionParameters"] = from_union([lambda x: from_list(
                lambda x: to_class(PurpleActionParameter, x), x), from_none], self.action_parameters)
        if self.requirement_type is not None:
            result["requirementType"] = from_union(
                [lambda x: to_enum(RequirementType, x), from_none], self.requirement_type)
        return result


@dataclass
class LoadRestriction:
    """Load restrictions for this edge. *Optional*."""

    loaded: bool
    """Indicates if the edge can be traversed with a load."""

    unloaded: bool
    """Indicates if the edge can be traversed without a load."""

    load_set_names: Optional[List[str]] = None
    """Names of the load sets allowed on this edge. *Optional*."""

    @staticmethod
    def from_dict(obj: Any) -> 'LoadRestriction':
        assert isinstance(obj, dict)
        loaded = from_bool(obj.get("loaded"))
        unloaded = from_bool(obj.get("unloaded"))
        load_set_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("loadSetNames"))
        return LoadRestriction(loaded, unloaded, load_set_names)

    def to_dict(self) -> dict:
        result: dict = {}
        result["loaded"] = from_bool(self.loaded)
        result["unloaded"] = from_bool(self.unloaded)
        if self.load_set_names is not None:
            result["loadSetNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.load_set_names)
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

    control_points: List[ControlPoint]
    """Control points defining the trajectory."""

    knot_vector: List[float]
    """Knot vector for the trajectory."""

    degree: Optional[int] = None
    """Degree of the trajectory curve. Default is 3. Range: [1 ... 3]"""

    @staticmethod
    def from_dict(obj: Any) -> 'Trajectory':
        assert isinstance(obj, dict)
        control_points = from_list(ControlPoint.from_dict, obj.get("controlPoints"))
        knot_vector = from_list(from_float, obj.get("knotVector"))
        degree = from_union([from_int, from_none], obj.get("degree"))
        return Trajectory(control_points, knot_vector, degree)

    def to_dict(self) -> dict:
        result: dict = {}
        result["controlPoints"] = from_list(lambda x: to_class(ControlPoint, x), self.control_points)
        result["knotVector"] = from_list(to_float, self.knot_vector)
        if self.degree is not None:
            result["degree"] = from_union([from_int, from_none], self.degree)
        return result


@dataclass
class VehicleTypeEdgeProperty:
    vehicle_type_id: str
    """Identifier for the vehicle type."""

    actions: Optional[List[VehicleTypeEdgePropertyAction]] = None
    """Actions that can be integrated into the order by the (third-party) master control system
    each time any vehicle with the corresponding vehicleTypeId is sent an order/order update
    that contains this edge. *Optional*.
    """
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

    reentry_allowed: Optional[bool] = None
    """true: Vehicles of the corresponding vehicleTypeId are allowed to enter into automatic
    management by the (third-party) master control system while on this edge. false: Vehicles
    are not allowed to enter into automatic management while on this edge. Default is true if
    not defined.
    """
    rotation_allowed: Optional[bool] = None
    """Indicates if rotation is allowed while on the edge. *Optional*."""

    rotation_at_end_node_allowed: Optional[str] = None
    """Specifies if rotation is allowed at the end node. *Optional*."""

    rotation_at_start_node_allowed: Optional[str] = None
    """Specifies if rotation is allowed at the start node. *Optional*."""

    trajectory: Optional[Trajectory] = None
    """Trajectory information for this edge, if applicable. *Optional*."""

    vehicle_orientation: Optional[float] = None
    """Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]"""

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeEdgeProperty':
        assert isinstance(obj, dict)
        vehicle_type_id = from_str(obj.get("vehicleTypeId"))
        actions = from_union([lambda x: from_list(VehicleTypeEdgePropertyAction.from_dict, x),
                             from_none], obj.get("actions"))
        load_restriction = from_union([LoadRestriction.from_dict, from_none], obj.get("loadRestriction"))
        max_height = from_union([from_float, from_none], obj.get("maxHeight"))
        max_rotation_speed = from_union([from_float, from_none], obj.get("maxRotationSpeed"))
        max_speed = from_union([from_float, from_none], obj.get("maxSpeed"))
        min_height = from_union([from_float, from_none], obj.get("minHeight"))
        orientation_type = from_union([from_str, from_none], obj.get("orientationType"))
        reentry_allowed = from_union([from_bool, from_none], obj.get("reentryAllowed"))
        rotation_allowed = from_union([from_bool, from_none], obj.get("rotationAllowed"))
        rotation_at_end_node_allowed = from_union([from_str, from_none], obj.get("rotationAtEndNodeAllowed"))
        rotation_at_start_node_allowed = from_union([from_str, from_none], obj.get("rotationAtStartNodeAllowed"))
        trajectory = from_union([Trajectory.from_dict, from_none], obj.get("trajectory"))
        vehicle_orientation = from_union([from_float, from_none], obj.get("vehicleOrientation"))
        return VehicleTypeEdgeProperty(vehicle_type_id, actions, load_restriction, max_height, max_rotation_speed, max_speed, min_height, orientation_type,
                                       reentry_allowed, rotation_allowed, rotation_at_end_node_allowed, rotation_at_start_node_allowed, trajectory, vehicle_orientation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["vehicleTypeId"] = from_str(self.vehicle_type_id)
        if self.actions is not None:
            result["actions"] = from_union([lambda x: from_list(lambda x: to_class(
                VehicleTypeEdgePropertyAction, x), x), from_none], self.actions)
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
        if self.reentry_allowed is not None:
            result["reentryAllowed"] = from_union([from_bool, from_none], self.reentry_allowed)
        if self.rotation_allowed is not None:
            result["rotationAllowed"] = from_union([from_bool, from_none], self.rotation_allowed)
        if self.rotation_at_end_node_allowed is not None:
            result["rotationAtEndNodeAllowed"] = from_union([from_str, from_none], self.rotation_at_end_node_allowed)
        if self.rotation_at_start_node_allowed is not None:
            result["rotationAtStartNodeAllowed"] = from_union(
                [from_str, from_none], self.rotation_at_start_node_allowed)
        if self.trajectory is not None:
            result["trajectory"] = from_union([lambda x: to_class(Trajectory, x), from_none], self.trajectory)
        if self.vehicle_orientation is not None:
            result["vehicleOrientation"] = from_union([to_float, from_none], self.vehicle_orientation)
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
class FluffyActionParameter:
    key: str
    """Key of the action parameter."""

    value: str
    """Value of the action parameter."""

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyActionParameter':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        value = from_str(obj.get("value"))
        return FluffyActionParameter(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["value"] = from_str(self.value)
        return result


@dataclass
class VehicleTypeNodePropertyAction:
    action_type: str
    """Type of action (e.g., move, load, unload)."""

    blocking_type: BlockingType
    """Specifies if the action is blocking. NONE: allows moving and other actions. SOFT: allows
    other actions, but not moving. HARD: is the only allowed action at this time.
    """
    action_description: Optional[str] = None
    """Description of the action. *Optional*."""

    action_parameters: Optional[List[FluffyActionParameter]] = None
    """Parameters associated with the action. *Optional*."""

    requirement_type: Optional[RequirementType] = None
    """Defines if the action is required. REQUIRED: The (third-party) master control system must
    always communicate this action. CONDITIONAL: The action may or may not be required
    contingent upon various factors. OPTIONAL: The action may or may not be communicated at
    the master control system's discretion.
    """

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeNodePropertyAction':
        assert isinstance(obj, dict)
        action_type = from_str(obj.get("actionType"))
        blocking_type = BlockingType(obj.get("blockingType"))
        action_description = from_union([from_str, from_none], obj.get("actionDescription"))
        action_parameters = from_union([lambda x: from_list(
            FluffyActionParameter.from_dict, x), from_none], obj.get("actionParameters"))
        requirement_type = from_union([RequirementType, from_none], obj.get("requirementType"))
        return VehicleTypeNodePropertyAction(action_type, blocking_type,
                                             action_description, action_parameters, requirement_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actionType"] = from_str(self.action_type)
        result["blockingType"] = to_enum(BlockingType, self.blocking_type)
        if self.action_description is not None:
            result["actionDescription"] = from_union([from_str, from_none], self.action_description)
        if self.action_parameters is not None:
            result["actionParameters"] = from_union([lambda x: from_list(
                lambda x: to_class(FluffyActionParameter, x), x), from_none], self.action_parameters)
        if self.requirement_type is not None:
            result["requirementType"] = from_union(
                [lambda x: to_enum(RequirementType, x), from_none], self.requirement_type)
        return result


@dataclass
class VehicleTypeNodeProperty:
    vehicle_type_id: str
    """Identifier for the vehicle type."""

    actions: Optional[List[VehicleTypeNodePropertyAction]] = None
    """List of actions that the vehicle can perform at the node. *Optional*."""

    theta: Optional[float] = None
    """Absolute orientation of the vehicle on the node in reference to the global origin’s
    rotation. Range: [-Pi ... Pi]
    """

    @staticmethod
    def from_dict(obj: Any) -> 'VehicleTypeNodeProperty':
        assert isinstance(obj, dict)
        vehicle_type_id = from_str(obj.get("vehicleTypeId"))
        actions = from_union([lambda x: from_list(VehicleTypeNodePropertyAction.from_dict, x),
                             from_none], obj.get("actions"))
        theta = from_union([from_float, from_none], obj.get("theta"))
        return VehicleTypeNodeProperty(vehicle_type_id, actions, theta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["vehicleTypeId"] = from_str(self.vehicle_type_id)
        if self.actions is not None:
            result["actions"] = from_union([lambda x: from_list(lambda x: to_class(
                VehicleTypeNodePropertyAction, x), x), from_none], self.actions)
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

    station_description: Optional[str] = None
    """Description of the station. *Optional*."""

    station_height: Optional[float] = None
    """Height of the station, if applicable, in meters. *Optional*. Range: [0.0 ... float64.max]"""

    station_name: Optional[str] = None
    """Name of the station. *Optional*."""

    station_position: Optional[StationPosition] = None
    """Position of the station on the map (in meters)."""

    @staticmethod
    def from_dict(obj: Any) -> 'Station':
        assert isinstance(obj, dict)
        interaction_node_ids = from_list(from_str, obj.get("interactionNodeIds"))
        station_id = from_str(obj.get("stationId"))
        station_description = from_union([from_str, from_none], obj.get("stationDescription"))
        station_height = from_union([from_float, from_none], obj.get("stationHeight"))
        station_name = from_union([from_str, from_none], obj.get("stationName"))
        station_position = from_union([StationPosition.from_dict, from_none], obj.get("stationPosition"))
        return Station(interaction_node_ids, station_id, station_description,
                       station_height, station_name, station_position)

    def to_dict(self) -> dict:
        result: dict = {}
        result["interactionNodeIds"] = from_list(from_str, self.interaction_node_ids)
        result["stationId"] = from_str(self.station_id)
        if self.station_description is not None:
            result["stationDescription"] = from_union([from_str, from_none], self.station_description)
        if self.station_height is not None:
            result["stationHeight"] = from_union([to_float, from_none], self.station_height)
        if self.station_name is not None:
            result["stationName"] = from_union([from_str, from_none], self.station_name)
        if self.station_position is not None:
            result["stationPosition"] = from_union(
                [lambda x: to_class(StationPosition, x), from_none], self.station_position)
        return result


@dataclass
class Layout:
    edges: List[Edge]
    """List of edges in the layout. Edges represent paths between nodes."""

    layout_id: str
    """Unique identifier for the layout."""

    layout_version: str
    """Version number of the layout. It is suggested that this be an integer, represented as a
    string, incremented with each change, starting at 1.
    """
    nodes: List[Node]
    """List of nodes in the layout. Nodes are locations where vehicles can navigate to."""

    stations: List[Station]
    """List of stations in the layout where vehicles perform specific actions."""

    layout_description: Optional[str] = None
    """Description of the layout. *Optional*."""

    layout_level_id: Optional[str] = None
    """Unique identifier for the layout level."""

    layout_name: Optional[str] = None
    """Name of the layout."""

    @staticmethod
    def from_dict(obj: Any) -> 'Layout':
        assert isinstance(obj, dict)
        edges = from_list(Edge.from_dict, obj.get("edges"))
        layout_id = from_str(obj.get("layoutId"))
        layout_version = from_str(obj.get("layoutVersion"))
        nodes = from_list(Node.from_dict, obj.get("nodes"))
        stations = from_list(Station.from_dict, obj.get("stations"))
        layout_description = from_union([from_str, from_none], obj.get("layoutDescription"))
        layout_level_id = from_union([from_str, from_none], obj.get("layoutLevelId"))
        layout_name = from_union([from_str, from_none], obj.get("layoutName"))
        return Layout(edges, layout_id, layout_version, nodes, stations,
                      layout_description, layout_level_id, layout_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["edges"] = from_list(lambda x: to_class(Edge, x), self.edges)
        result["layoutId"] = from_str(self.layout_id)
        result["layoutVersion"] = from_str(self.layout_version)
        result["nodes"] = from_list(lambda x: to_class(Node, x), self.nodes)
        result["stations"] = from_list(lambda x: to_class(Station, x), self.stations)
        if self.layout_description is not None:
            result["layoutDescription"] = from_union([from_str, from_none], self.layout_description)
        if self.layout_level_id is not None:
            result["layoutLevelId"] = from_union([from_str, from_none], self.layout_level_id)
        if self.layout_name is not None:
            result["layoutName"] = from_union([from_str, from_none], self.layout_name)
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
