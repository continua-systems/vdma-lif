# Table of Contents

* [vdma\_lif.models](#vdma_lif.models)
  * [LoadRestriction](#vdma_lif.models.LoadRestriction)
    * [loaded](#vdma_lif.models.LoadRestriction.loaded)
    * [load\_set\_names](#vdma_lif.models.LoadRestriction.load_set_names)
    * [unloaded](#vdma_lif.models.LoadRestriction.unloaded)
  * [ControlPoint](#vdma_lif.models.ControlPoint)
    * [x](#vdma_lif.models.ControlPoint.x)
    * [y](#vdma_lif.models.ControlPoint.y)
    * [weight](#vdma_lif.models.ControlPoint.weight)
  * [Trajectory](#vdma_lif.models.Trajectory)
    * [control\_points](#vdma_lif.models.Trajectory.control_points)
    * [degree](#vdma_lif.models.Trajectory.degree)
    * [knot\_vector](#vdma_lif.models.Trajectory.knot_vector)
  * [VehicleTypeEdgeProperty](#vdma_lif.models.VehicleTypeEdgeProperty)
    * [vehicle\_orientation](#vdma_lif.models.VehicleTypeEdgeProperty.vehicle_orientation)
    * [vehicle\_type\_id](#vdma_lif.models.VehicleTypeEdgeProperty.vehicle_type_id)
    * [load\_restriction](#vdma_lif.models.VehicleTypeEdgeProperty.load_restriction)
    * [max\_height](#vdma_lif.models.VehicleTypeEdgeProperty.max_height)
    * [max\_rotation\_speed](#vdma_lif.models.VehicleTypeEdgeProperty.max_rotation_speed)
    * [max\_speed](#vdma_lif.models.VehicleTypeEdgeProperty.max_speed)
    * [min\_height](#vdma_lif.models.VehicleTypeEdgeProperty.min_height)
    * [orientation\_type](#vdma_lif.models.VehicleTypeEdgeProperty.orientation_type)
    * [rotation\_allowed](#vdma_lif.models.VehicleTypeEdgeProperty.rotation_allowed)
    * [rotation\_at\_end\_node\_allowed](#vdma_lif.models.VehicleTypeEdgeProperty.rotation_at_end_node_allowed)
    * [rotation\_at\_start\_node\_allowed](#vdma_lif.models.VehicleTypeEdgeProperty.rotation_at_start_node_allowed)
    * [trajectory](#vdma_lif.models.VehicleTypeEdgeProperty.trajectory)
  * [Edge](#vdma_lif.models.Edge)
    * [edge\_id](#vdma_lif.models.Edge.edge_id)
    * [end\_node\_id](#vdma_lif.models.Edge.end_node_id)
    * [start\_node\_id](#vdma_lif.models.Edge.start_node_id)
    * [vehicle\_type\_edge\_properties](#vdma_lif.models.Edge.vehicle_type_edge_properties)
  * [NodePosition](#vdma_lif.models.NodePosition)
    * [x](#vdma_lif.models.NodePosition.x)
    * [y](#vdma_lif.models.NodePosition.y)
  * [ActionParameter](#vdma_lif.models.ActionParameter)
    * [key](#vdma_lif.models.ActionParameter.key)
    * [value](#vdma_lif.models.ActionParameter.value)
  * [Action](#vdma_lif.models.Action)
    * [action\_description](#vdma_lif.models.Action.action_description)
    * [action\_parameters](#vdma_lif.models.Action.action_parameters)
    * [action\_type](#vdma_lif.models.Action.action_type)
    * [blocking\_type](#vdma_lif.models.Action.blocking_type)
    * [required](#vdma_lif.models.Action.required)
  * [VehicleTypeNodeProperty](#vdma_lif.models.VehicleTypeNodeProperty)
    * [theta](#vdma_lif.models.VehicleTypeNodeProperty.theta)
    * [vehicle\_type\_id](#vdma_lif.models.VehicleTypeNodeProperty.vehicle_type_id)
    * [actions](#vdma_lif.models.VehicleTypeNodeProperty.actions)
  * [Node](#vdma_lif.models.Node)
    * [node\_id](#vdma_lif.models.Node.node_id)
    * [node\_position](#vdma_lif.models.Node.node_position)
    * [vehicle\_type\_node\_properties](#vdma_lif.models.Node.vehicle_type_node_properties)
    * [map\_id](#vdma_lif.models.Node.map_id)
    * [node\_description](#vdma_lif.models.Node.node_description)
    * [node\_name](#vdma_lif.models.Node.node_name)
  * [StationPosition](#vdma_lif.models.StationPosition)
    * [x](#vdma_lif.models.StationPosition.x)
    * [y](#vdma_lif.models.StationPosition.y)
    * [theta](#vdma_lif.models.StationPosition.theta)
  * [Station](#vdma_lif.models.Station)
    * [interaction\_node\_ids](#vdma_lif.models.Station.interaction_node_ids)
    * [station\_id](#vdma_lif.models.Station.station_id)
    * [station\_position](#vdma_lif.models.Station.station_position)
    * [station\_description](#vdma_lif.models.Station.station_description)
    * [station\_height](#vdma_lif.models.Station.station_height)
    * [station\_name](#vdma_lif.models.Station.station_name)
  * [Layout](#vdma_lif.models.Layout)
    * [edges](#vdma_lif.models.Layout.edges)
    * [layout\_id](#vdma_lif.models.Layout.layout_id)
    * [nodes](#vdma_lif.models.Layout.nodes)
    * [layout\_description](#vdma_lif.models.Layout.layout_description)
    * [layout\_level\_id](#vdma_lif.models.Layout.layout_level_id)
    * [layout\_name](#vdma_lif.models.Layout.layout_name)
    * [layout\_version](#vdma_lif.models.Layout.layout_version)
    * [stations](#vdma_lif.models.Layout.stations)
  * [MetaInformation](#vdma_lif.models.MetaInformation)
    * [creator](#vdma_lif.models.MetaInformation.creator)
    * [export\_timestamp](#vdma_lif.models.MetaInformation.export_timestamp)
    * [lif\_version](#vdma_lif.models.MetaInformation.lif_version)
    * [project\_identification](#vdma_lif.models.MetaInformation.project_identification)
  * [LIFSchema](#vdma_lif.models.LIFSchema)
    * [layouts](#vdma_lif.models.LIFSchema.layouts)
    * [meta\_information](#vdma_lif.models.LIFSchema.meta_information)

<a id="vdma_lif.models"></a>

# vdma\_lif.models

<a id="vdma_lif.models.LoadRestriction"></a>

## LoadRestriction Objects

```python
@dataclass
class LoadRestriction()
```

Load restrictions for this edge. *Optional*.

<a id="vdma_lif.models.LoadRestriction.loaded"></a>

#### loaded

Indicates if the edge can be traversed with a load.

<a id="vdma_lif.models.LoadRestriction.load_set_names"></a>

#### load\_set\_names

Names of the load sets allowed on this edge. *Optional*.

<a id="vdma_lif.models.LoadRestriction.unloaded"></a>

#### unloaded

Indicates if the edge can be traversed without a load.

<a id="vdma_lif.models.ControlPoint"></a>

## ControlPoint Objects

```python
@dataclass
class ControlPoint()
```

<a id="vdma_lif.models.ControlPoint.x"></a>

#### x

X coordinate of the control point in millimeters.

<a id="vdma_lif.models.ControlPoint.y"></a>

#### y

Y coordinate of the control point in millimeters.

<a id="vdma_lif.models.ControlPoint.weight"></a>

#### weight

The weight with which this control point pulls on the curve. When not defined, the
default is 1.0. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.Trajectory"></a>

## Trajectory Objects

```python
@dataclass
class Trajectory()
```

Trajectory information for this edge, if applicable. *Optional*.

<a id="vdma_lif.models.Trajectory.control_points"></a>

#### control\_points

Control points defining the trajectory. *Optional*.

<a id="vdma_lif.models.Trajectory.degree"></a>

#### degree

Degree of the trajectory curve. Default is 3. Range: [1 ... 3]

<a id="vdma_lif.models.Trajectory.knot_vector"></a>

#### knot\_vector

Knot vector for the trajectory. *Optional*.

<a id="vdma_lif.models.VehicleTypeEdgeProperty"></a>

## VehicleTypeEdgeProperty Objects

```python
@dataclass
class VehicleTypeEdgeProperty()
```

<a id="vdma_lif.models.VehicleTypeEdgeProperty.vehicle_orientation"></a>

#### vehicle\_orientation

Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]

<a id="vdma_lif.models.VehicleTypeEdgeProperty.vehicle_type_id"></a>

#### vehicle\_type\_id

Identifier for the vehicle type.

<a id="vdma_lif.models.VehicleTypeEdgeProperty.load_restriction"></a>

#### load\_restriction

Load restrictions for this edge. *Optional*.

<a id="vdma_lif.models.VehicleTypeEdgeProperty.max_height"></a>

#### max\_height

Maximum height of the vehicle on this edge in millimeters. *Optional*. Range: [0.0 ...
float64.max]

<a id="vdma_lif.models.VehicleTypeEdgeProperty.max_rotation_speed"></a>

#### max\_rotation\_speed

Maximum rotation speed allowed on this edge in radians per second. *Optional*. Range:
[0.0 ... float64.max]

<a id="vdma_lif.models.VehicleTypeEdgeProperty.max_speed"></a>

#### max\_speed

Maximum speed allowed on this edge in meters per second. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.VehicleTypeEdgeProperty.min_height"></a>

#### min\_height

Minimum height of the vehicle on this edge in millimeters. *Optional*. Range: [0.0 ...
float64.max]

<a id="vdma_lif.models.VehicleTypeEdgeProperty.orientation_type"></a>

#### orientation\_type

Type of orientation (e.g., TANGENTIAL).

<a id="vdma_lif.models.VehicleTypeEdgeProperty.rotation_allowed"></a>

#### rotation\_allowed

Indicates if rotation is allowed while on the edge. *Optional*.

<a id="vdma_lif.models.VehicleTypeEdgeProperty.rotation_at_end_node_allowed"></a>

#### rotation\_at\_end\_node\_allowed

Specifies if rotation is allowed at the end node. *Optional*.

<a id="vdma_lif.models.VehicleTypeEdgeProperty.rotation_at_start_node_allowed"></a>

#### rotation\_at\_start\_node\_allowed

Specifies if rotation is allowed at the start node. *Optional*.

<a id="vdma_lif.models.VehicleTypeEdgeProperty.trajectory"></a>

#### trajectory

Trajectory information for this edge, if applicable. *Optional*.

<a id="vdma_lif.models.Edge"></a>

## Edge Objects

```python
@dataclass
class Edge()
```

<a id="vdma_lif.models.Edge.edge_id"></a>

#### edge\_id

Unique identifier for the edge.

<a id="vdma_lif.models.Edge.end_node_id"></a>

#### end\_node\_id

ID of the ending node for this edge.

<a id="vdma_lif.models.Edge.start_node_id"></a>

#### start\_node\_id

ID of the starting node for this edge.

<a id="vdma_lif.models.Edge.vehicle_type_edge_properties"></a>

#### vehicle\_type\_edge\_properties

Vehicle-specific properties for the edge.

<a id="vdma_lif.models.NodePosition"></a>

## NodePosition Objects

```python
@dataclass
class NodePosition()
```

Position of the node on the map (in millimeters).

<a id="vdma_lif.models.NodePosition.x"></a>

#### x

X coordinate of the node in millimeters. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.NodePosition.y"></a>

#### y

Y coordinate of the node in millimeters. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.ActionParameter"></a>

## ActionParameter Objects

```python
@dataclass
class ActionParameter()
```

<a id="vdma_lif.models.ActionParameter.key"></a>

#### key

Key of the action parameter.

<a id="vdma_lif.models.ActionParameter.value"></a>

#### value

Value of the action parameter.

<a id="vdma_lif.models.Action"></a>

## Action Objects

```python
@dataclass
class Action()
```

<a id="vdma_lif.models.Action.action_description"></a>

#### action\_description

Description of the action. *Optional*.

<a id="vdma_lif.models.Action.action_parameters"></a>

#### action\_parameters

Parameters associated with the action. *Optional*.

<a id="vdma_lif.models.Action.action_type"></a>

#### action\_type

Type of action (e.g., move, load, unload).

<a id="vdma_lif.models.Action.blocking_type"></a>

#### blocking\_type

Specifies if the action is blocking (HARD or SOFT).

<a id="vdma_lif.models.Action.required"></a>

#### required

Whether the action is mandatory.

<a id="vdma_lif.models.VehicleTypeNodeProperty"></a>

## VehicleTypeNodeProperty Objects

```python
@dataclass
class VehicleTypeNodeProperty()
```

<a id="vdma_lif.models.VehicleTypeNodeProperty.theta"></a>

#### theta

Orientation of the vehicle at the node in degrees. Range: [0.0 ... 360.0]

<a id="vdma_lif.models.VehicleTypeNodeProperty.vehicle_type_id"></a>

#### vehicle\_type\_id

Identifier for the vehicle type.

<a id="vdma_lif.models.VehicleTypeNodeProperty.actions"></a>

#### actions

List of actions that the vehicle can perform at the node. *Optional*.

<a id="vdma_lif.models.Node"></a>

## Node Objects

```python
@dataclass
class Node()
```

<a id="vdma_lif.models.Node.node_id"></a>

#### node\_id

Unique identifier for the node.

<a id="vdma_lif.models.Node.node_position"></a>

#### node\_position

Position of the node on the map (in millimeters).

<a id="vdma_lif.models.Node.vehicle_type_node_properties"></a>

#### vehicle\_type\_node\_properties

Vehicle-specific properties related to the node.

<a id="vdma_lif.models.Node.map_id"></a>

#### map\_id

Identifier for the map that this node belongs to. *Optional*.

<a id="vdma_lif.models.Node.node_description"></a>

#### node\_description

Description of the node. *Optional*.

<a id="vdma_lif.models.Node.node_name"></a>

#### node\_name

Name of the node. *Optional*.

<a id="vdma_lif.models.StationPosition"></a>

## StationPosition Objects

```python
@dataclass
class StationPosition()
```

Position of the station on the map (in millimeters).

<a id="vdma_lif.models.StationPosition.x"></a>

#### x

X coordinate of the station in millimeters. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.StationPosition.y"></a>

#### y

Y coordinate of the station in millimeters. Range: [0.0 ... float64.max]

<a id="vdma_lif.models.StationPosition.theta"></a>

#### theta

Orientation of the station in degrees. Unit: radians. Range: [-Pi ... Pi]

<a id="vdma_lif.models.Station"></a>

## Station Objects

```python
@dataclass
class Station()
```

<a id="vdma_lif.models.Station.interaction_node_ids"></a>

#### interaction\_node\_ids

List of node IDs where the station interacts.

<a id="vdma_lif.models.Station.station_id"></a>

#### station\_id

Unique identifier for the station.

<a id="vdma_lif.models.Station.station_position"></a>

#### station\_position

Position of the station on the map (in millimeters).

<a id="vdma_lif.models.Station.station_description"></a>

#### station\_description

Description of the station. *Optional*.

<a id="vdma_lif.models.Station.station_height"></a>

#### station\_height

Height of the station, if applicable, in millimeters. *Optional*. Range: [0.0 ...
float64.max]

<a id="vdma_lif.models.Station.station_name"></a>

#### station\_name

Name of the station. *Optional*.

<a id="vdma_lif.models.Layout"></a>

## Layout Objects

```python
@dataclass
class Layout()
```

<a id="vdma_lif.models.Layout.edges"></a>

#### edges

List of edges in the layout. Edges represent paths between nodes.

<a id="vdma_lif.models.Layout.layout_id"></a>

#### layout\_id

Unique identifier for the layout.

<a id="vdma_lif.models.Layout.nodes"></a>

#### nodes

List of nodes in the layout. Nodes are locations where vehicles can navigate to.

<a id="vdma_lif.models.Layout.layout_description"></a>

#### layout\_description

Description of the layout. *Optional*.

<a id="vdma_lif.models.Layout.layout_level_id"></a>

#### layout\_level\_id

Unique identifier for the layout level.

<a id="vdma_lif.models.Layout.layout_name"></a>

#### layout\_name

Name of the layout.

<a id="vdma_lif.models.Layout.layout_version"></a>

#### layout\_version

Version number of the layout.

<a id="vdma_lif.models.Layout.stations"></a>

#### stations

List of stations in the layout where vehicles perform specific actions.

<a id="vdma_lif.models.MetaInformation"></a>

## MetaInformation Objects

```python
@dataclass
class MetaInformation()
```

Contains metadata about the project and the LIF file.

<a id="vdma_lif.models.MetaInformation.creator"></a>

#### creator

Creator of the LIF file (e.g., name of company or person).

<a id="vdma_lif.models.MetaInformation.export_timestamp"></a>

#### export\_timestamp

The timestamp at which this LIF file was created/updated/modified. Format is ISO8601 in
UTC.

<a id="vdma_lif.models.MetaInformation.lif_version"></a>

#### lif\_version

Version of the LIF file format. Follows semantic versioning (Major.Minor.Patch).

<a id="vdma_lif.models.MetaInformation.project_identification"></a>

#### project\_identification

Human-readable name of the project (e.g., for display purposes).

<a id="vdma_lif.models.LIFSchema"></a>

## LIFSchema Objects

```python
@dataclass
class LIFSchema()
```

<a id="vdma_lif.models.LIFSchema.layouts"></a>

#### layouts

Collection of layouts used in the facility by the driverless transport system. All
layouts refer to the same global origin.

<a id="vdma_lif.models.LIFSchema.meta_information"></a>

#### meta\_information

Contains metadata about the project and the LIF file.

