// To parse this data:
//
//   import { Convert, LIFLayoutCollection } from "./file";
//
//   const lIFLayoutCollection = Convert.toLIFLayoutCollection(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface LIFLayoutCollection {
  /**
   * Collection of layouts used in the facility by the driverless transport system. All
   * layouts refer to the same global origin.
   */
  layouts: Layout[];
  /**
   * Contains metadata about the project and the LIF file.
   */
  metaInformation: MetaInformation;
  [property: string]: any;
}

export interface Layout {
  /**
   * List of edges in the layout. Edges represent paths between nodes.
   */
  edges: Edge[];
  /**
   * Description of the layout. *Optional*.
   */
  layoutDescription?: string;
  /**
   * Unique identifier for the layout.
   */
  layoutId: string;
  /**
   * Unique identifier for the layout level.
   */
  layoutLevelId?: string;
  /**
   * Name of the layout.
   */
  layoutName?: string;
  /**
   * Version number of the layout. It is suggested that this be an integer, represented as a
   * string, incremented with each change, starting at 1.
   */
  layoutVersion: string;
  /**
   * List of nodes in the layout. Nodes are locations where vehicles can navigate to.
   */
  nodes: Node[];
  /**
   * List of stations in the layout where vehicles perform specific actions.
   */
  stations: Station[];
  [property: string]: any;
}

export interface Edge {
  /**
   * Unique identifier for the edge.
   */
  edgeId: string;
  /**
   * ID of the ending node for this edge.
   */
  endNodeId: string;
  /**
   * ID of the starting node for this edge.
   */
  startNodeId: string;
  /**
   * Vehicle-specific properties for the edge.
   */
  vehicleTypeEdgeProperties: VehicleTypeEdgeProperty[];
  [property: string]: any;
}

export interface VehicleTypeEdgeProperty {
  /**
   * Load restrictions for this edge. *Optional*.
   */
  loadRestriction?: LoadRestriction;
  /**
   * Maximum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
   * float64.max]
   */
  maxHeight?: number;
  /**
   * Maximum rotation speed allowed on this edge in radians per second. *Optional*. Range:
   * [0.0 ... float64.max]
   */
  maxRotationSpeed?: number;
  /**
   * Maximum speed allowed on this edge in meters per second. Range: [0.0 ... float64.max]
   */
  maxSpeed?: number;
  /**
   * Minimum height of the vehicle on this edge in meters. *Optional*. Range: [0.0 ...
   * float64.max]
   */
  minHeight?: number;
  /**
   * Type of orientation (e.g., TANGENTIAL).
   */
  orientationType?: string;
  /**
   * Indicates if rotation is allowed while on the edge. *Optional*.
   */
  rotationAllowed?: boolean;
  /**
   * Specifies if rotation is allowed at the end node. *Optional*.
   */
  rotationAtEndNodeAllowed?: string;
  /**
   * Specifies if rotation is allowed at the start node. *Optional*.
   */
  rotationAtStartNodeAllowed?: string;
  /**
   * Trajectory information for this edge, if applicable. *Optional*.
   */
  trajectory?: Trajectory;
  /**
   * Orientation of the vehicle while traversing the edge, in degrees. Range: [0.0 ... 360.0]
   */
  vehicleOrientation?: number;
  /**
   * Identifier for the vehicle type.
   */
  vehicleTypeId: string;
  [property: string]: any;
}

/**
 * Load restrictions for this edge. *Optional*.
 */
export interface LoadRestriction {
  /**
   * Indicates if the edge can be traversed with a load.
   */
  loaded: boolean;
  /**
   * Names of the load sets allowed on this edge. *Optional*.
   */
  loadSetNames?: string[];
  /**
   * Indicates if the edge can be traversed without a load.
   */
  unloaded: boolean;
  [property: string]: any;
}

/**
 * Trajectory information for this edge, if applicable. *Optional*.
 */
export interface Trajectory {
  /**
   * Control points defining the trajectory.
   */
  controlPoints: ControlPoint[];
  /**
   * Degree of the trajectory curve. Default is 3. Range: [1 ... 3]
   */
  degree?: number;
  /**
   * Knot vector for the trajectory.
   */
  knotVector: number[];
  [property: string]: any;
}

export interface ControlPoint {
  /**
   * The weight with which this control point pulls on the curve. When not defined, the
   * default is 1.0. Range: [0.0 ... float64.max]
   */
  weight?: number;
  /**
   * X coordinate of the control point in meters.
   */
  x: number;
  /**
   * Y coordinate of the control point in meters.
   */
  y: number;
  [property: string]: any;
}

export interface Node {
  /**
   * Identifier for the map that this node belongs to. *Optional*.
   */
  mapId?: string;
  /**
   * Description of the node. *Optional*.
   */
  nodeDescription?: string;
  /**
   * Unique identifier for the node.
   */
  nodeId: string;
  /**
   * Name of the node. *Optional*.
   */
  nodeName?: string;
  /**
   * Position of the node on the map (in meters).
   */
  nodePosition: NodePosition;
  /**
   * Vehicle-specific properties related to the node.
   */
  vehicleTypeNodeProperties: VehicleTypeNodeProperty[];
  [property: string]: any;
}

/**
 * Position of the node on the map (in meters).
 */
export interface NodePosition {
  /**
   * X coordinate of the node in meters. Range: [float64.min ... float64.max]
   */
  x: number;
  /**
   * Y coordinate of the node in meters. Range: [float64.min... float64.max]
   */
  y: number;
  [property: string]: any;
}

export interface VehicleTypeNodeProperty {
  /**
   * List of actions that the vehicle can perform at the node. *Optional*.
   */
  actions?: Action[];
  /**
   * Absolute orientation of the vehicle on the node in reference to the global origin’s
   * rotation. Range: [-Pi ... Pi]
   */
  theta?: number;
  /**
   * Identifier for the vehicle type.
   */
  vehicleTypeId: string;
  [property: string]: any;
}

export interface Action {
  /**
   * Description of the action. *Optional*.
   */
  actionDescription?: string;
  /**
   * Parameters associated with the action. *Optional*.
   */
  actionParameters?: ActionParameter[];
  /**
   * Type of action (e.g., move, load, unload).
   */
  actionType: string;
  /**
   * Specifies if the action is blocking (HARD or SOFT).
   */
  blockingType: string;
  /**
   * Whether the action is mandatory.
   */
  required?: boolean;
  [property: string]: any;
}

export interface ActionParameter {
  /**
   * Key of the action parameter.
   */
  key: string;
  /**
   * Value of the action parameter.
   */
  value: string;
  [property: string]: any;
}

export interface Station {
  /**
   * List of node IDs where the station interacts.
   */
  interactionNodeIds: string[];
  /**
   * Description of the station. *Optional*.
   */
  stationDescription?: string;
  /**
   * Height of the station, if applicable, in meters. *Optional*. Range: [0.0 ... float64.max]
   */
  stationHeight?: number;
  /**
   * Unique identifier for the station.
   */
  stationId: string;
  /**
   * Name of the station. *Optional*.
   */
  stationName?: string;
  /**
   * Position of the station on the map (in meters).
   */
  stationPosition?: StationPosition;
  [property: string]: any;
}

/**
 * Position of the station on the map (in meters).
 */
export interface StationPosition {
  /**
   * Orientation of the station. Unit: radians. Range: [-Pi ... Pi]
   */
  theta?: number;
  /**
   * X coordinate of the station in meters. Range: [float64.min ... float64.max]
   */
  x: number;
  /**
   * Y coordinate of the station in meters. Range: [float64.min ... float64.max]
   */
  y: number;
  [property: string]: any;
}

/**
 * Contains metadata about the project and the LIF file.
 */
export interface MetaInformation {
  /**
   * Creator of the LIF file (e.g., name of company or person).
   */
  creator: string;
  /**
   * The timestamp at which this LIF file was created/updated/modified. Format is ISO8601 in
   * UTC.
   */
  exportTimestamp: Date;
  /**
   * Version of the LIF file format. Follows semantic versioning (Major.Minor.Patch).
   */
  lifVersion: string;
  /**
   * Human-readable name of the project (e.g., for display purposes).
   */
  projectIdentification: string;
  [property: string]: any;
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
  public static toLIFLayoutCollection(json: string): LIFLayoutCollection {
    return cast(JSON.parse(json), r("LIFLayoutCollection"));
  }

  public static lIFLayoutCollectionToJson(value: LIFLayoutCollection): string {
    return JSON.stringify(uncast(value, r("LIFLayoutCollection")), null, 2);
  }
}

function invalidValue(typ: any, val: any, key: any, parent: any = ""): never {
  const prettyTyp = prettyTypeName(typ);
  const parentText = parent ? ` on ${parent}` : "";
  const keyText = key ? ` for key "${key}"` : "";
  throw Error(
    `Invalid value${keyText}${parentText}. Expected ${prettyTyp} but got ${JSON.stringify(val)}`,
  );
}

function prettyTypeName(typ: any): string {
  if (Array.isArray(typ)) {
    if (typ.length === 2 && typ[0] === undefined) {
      return `an optional ${prettyTypeName(typ[1])}`;
    } else {
      return `one of [${typ
        .map((a) => {
          return prettyTypeName(a);
        })
        .join(", ")}]`;
    }
  } else if (typeof typ === "object" && typ.literal !== undefined) {
    return typ.literal;
  } else {
    return typeof typ;
  }
}

function jsonToJSProps(typ: any): any {
  if (typ.jsonToJS === undefined) {
    const map: any = {};
    typ.props.forEach((p: any) => (map[p.json] = { key: p.js, typ: p.typ }));
    typ.jsonToJS = map;
  }
  return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
  if (typ.jsToJSON === undefined) {
    const map: any = {};
    typ.props.forEach((p: any) => (map[p.js] = { key: p.json, typ: p.typ }));
    typ.jsToJSON = map;
  }
  return typ.jsToJSON;
}

function transform(
  val: any,
  typ: any,
  getProps: any,
  key: any = "",
  parent: any = "",
): any {
  function transformPrimitive(typ: string, val: any): any {
    if (typeof typ === typeof val) return val;
    return invalidValue(typ, val, key, parent);
  }

  function transformUnion(typs: any[], val: any): any {
    // val must validate against one typ in typs
    const l = typs.length;
    for (let i = 0; i < l; i++) {
      const typ = typs[i];
      try {
        return transform(val, typ, getProps);
      } catch (_) {}
    }
    return invalidValue(typs, val, key, parent);
  }

  function transformEnum(cases: string[], val: any): any {
    if (cases.indexOf(val) !== -1) return val;
    return invalidValue(
      cases.map((a) => {
        return l(a);
      }),
      val,
      key,
      parent,
    );
  }

  function transformArray(typ: any, val: any): any {
    // val must be an array with no invalid elements
    if (!Array.isArray(val)) return invalidValue(l("array"), val, key, parent);
    return val.map((el) => transform(el, typ, getProps));
  }

  function transformDate(val: any): any {
    if (val === null) {
      return null;
    }
    const d = new Date(val);
    if (isNaN(d.valueOf())) {
      return invalidValue(l("Date"), val, key, parent);
    }
    return d;
  }

  function transformObject(
    props: { [k: string]: any },
    additional: any,
    val: any,
  ): any {
    if (val === null || typeof val !== "object" || Array.isArray(val)) {
      return invalidValue(l(ref || "object"), val, key, parent);
    }
    const result: any = {};
    Object.getOwnPropertyNames(props).forEach((key) => {
      const prop = props[key];
      const v = Object.prototype.hasOwnProperty.call(val, key)
        ? val[key]
        : undefined;
      result[prop.key] = transform(v, prop.typ, getProps, key, ref);
    });
    Object.getOwnPropertyNames(val).forEach((key) => {
      if (!Object.prototype.hasOwnProperty.call(props, key)) {
        result[key] = transform(val[key], additional, getProps, key, ref);
      }
    });
    return result;
  }

  if (typ === "any") return val;
  if (typ === null) {
    if (val === null) return val;
    return invalidValue(typ, val, key, parent);
  }
  if (typ === false) return invalidValue(typ, val, key, parent);
  let ref: any = undefined;
  while (typeof typ === "object" && typ.ref !== undefined) {
    ref = typ.ref;
    typ = typeMap[typ.ref];
  }
  if (Array.isArray(typ)) return transformEnum(typ, val);
  if (typeof typ === "object") {
    return typ.hasOwnProperty("unionMembers")
      ? transformUnion(typ.unionMembers, val)
      : typ.hasOwnProperty("arrayItems")
        ? transformArray(typ.arrayItems, val)
        : typ.hasOwnProperty("props")
          ? transformObject(getProps(typ), typ.additional, val)
          : invalidValue(typ, val, key, parent);
  }
  // Numbers can be parsed by Date but shouldn't be.
  if (typ === Date && typeof val !== "number") return transformDate(val);
  return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
  return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
  return transform(val, typ, jsToJSONProps);
}

function l(typ: any) {
  return { literal: typ };
}

function a(typ: any) {
  return { arrayItems: typ };
}

function u(...typs: any[]) {
  return { unionMembers: typs };
}

function o(props: any[], additional: any) {
  return { props, additional };
}

function m(additional: any) {
  return { props: [], additional };
}

function r(name: string) {
  return { ref: name };
}

const typeMap: any = {
  LIFLayoutCollection: o(
    [
      { json: "layouts", js: "layouts", typ: a(r("Layout")) },
      {
        json: "metaInformation",
        js: "metaInformation",
        typ: r("MetaInformation"),
      },
    ],
    "any",
  ),
  Layout: o(
    [
      { json: "edges", js: "edges", typ: a(r("Edge")) },
      {
        json: "layoutDescription",
        js: "layoutDescription",
        typ: u(undefined, ""),
      },
      { json: "layoutId", js: "layoutId", typ: "" },
      { json: "layoutLevelId", js: "layoutLevelId", typ: u(undefined, "") },
      { json: "layoutName", js: "layoutName", typ: u(undefined, "") },
      { json: "layoutVersion", js: "layoutVersion", typ: "" },
      { json: "nodes", js: "nodes", typ: a(r("Node")) },
      { json: "stations", js: "stations", typ: a(r("Station")) },
    ],
    "any",
  ),
  Edge: o(
    [
      { json: "edgeId", js: "edgeId", typ: "" },
      { json: "endNodeId", js: "endNodeId", typ: "" },
      { json: "startNodeId", js: "startNodeId", typ: "" },
      {
        json: "vehicleTypeEdgeProperties",
        js: "vehicleTypeEdgeProperties",
        typ: a(r("VehicleTypeEdgeProperty")),
      },
    ],
    "any",
  ),
  VehicleTypeEdgeProperty: o(
    [
      {
        json: "loadRestriction",
        js: "loadRestriction",
        typ: u(undefined, r("LoadRestriction")),
      },
      { json: "maxHeight", js: "maxHeight", typ: u(undefined, 3.14) },
      {
        json: "maxRotationSpeed",
        js: "maxRotationSpeed",
        typ: u(undefined, 3.14),
      },
      { json: "maxSpeed", js: "maxSpeed", typ: u(undefined, 3.14) },
      { json: "minHeight", js: "minHeight", typ: u(undefined, 3.14) },
      { json: "orientationType", js: "orientationType", typ: u(undefined, "") },
      {
        json: "rotationAllowed",
        js: "rotationAllowed",
        typ: u(undefined, true),
      },
      {
        json: "rotationAtEndNodeAllowed",
        js: "rotationAtEndNodeAllowed",
        typ: u(undefined, ""),
      },
      {
        json: "rotationAtStartNodeAllowed",
        js: "rotationAtStartNodeAllowed",
        typ: u(undefined, ""),
      },
      {
        json: "trajectory",
        js: "trajectory",
        typ: u(undefined, r("Trajectory")),
      },
      {
        json: "vehicleOrientation",
        js: "vehicleOrientation",
        typ: u(undefined, 3.14),
      },
      { json: "vehicleTypeId", js: "vehicleTypeId", typ: "" },
    ],
    "any",
  ),
  LoadRestriction: o(
    [
      { json: "loaded", js: "loaded", typ: true },
      { json: "loadSetNames", js: "loadSetNames", typ: u(undefined, a("")) },
      { json: "unloaded", js: "unloaded", typ: true },
    ],
    "any",
  ),
  Trajectory: o(
    [
      { json: "controlPoints", js: "controlPoints", typ: a(r("ControlPoint")) },
      { json: "degree", js: "degree", typ: u(undefined, 0) },
      { json: "knotVector", js: "knotVector", typ: a(3.14) },
    ],
    "any",
  ),
  ControlPoint: o(
    [
      { json: "weight", js: "weight", typ: u(undefined, 3.14) },
      { json: "x", js: "x", typ: 3.14 },
      { json: "y", js: "y", typ: 3.14 },
    ],
    "any",
  ),
  Node: o(
    [
      { json: "mapId", js: "mapId", typ: u(undefined, "") },
      { json: "nodeDescription", js: "nodeDescription", typ: u(undefined, "") },
      { json: "nodeId", js: "nodeId", typ: "" },
      { json: "nodeName", js: "nodeName", typ: u(undefined, "") },
      { json: "nodePosition", js: "nodePosition", typ: r("NodePosition") },
      {
        json: "vehicleTypeNodeProperties",
        js: "vehicleTypeNodeProperties",
        typ: a(r("VehicleTypeNodeProperty")),
      },
    ],
    "any",
  ),
  NodePosition: o(
    [
      { json: "x", js: "x", typ: 3.14 },
      { json: "y", js: "y", typ: 3.14 },
    ],
    "any",
  ),
  VehicleTypeNodeProperty: o(
    [
      { json: "actions", js: "actions", typ: u(undefined, a(r("Action"))) },
      { json: "theta", js: "theta", typ: u(undefined, 3.14) },
      { json: "vehicleTypeId", js: "vehicleTypeId", typ: "" },
    ],
    "any",
  ),
  Action: o(
    [
      {
        json: "actionDescription",
        js: "actionDescription",
        typ: u(undefined, ""),
      },
      {
        json: "actionParameters",
        js: "actionParameters",
        typ: u(undefined, a(r("ActionParameter"))),
      },
      { json: "actionType", js: "actionType", typ: "" },
      { json: "blockingType", js: "blockingType", typ: "" },
      { json: "required", js: "required", typ: u(undefined, true) },
    ],
    "any",
  ),
  ActionParameter: o(
    [
      { json: "key", js: "key", typ: "" },
      { json: "value", js: "value", typ: "" },
    ],
    "any",
  ),
  Station: o(
    [
      { json: "interactionNodeIds", js: "interactionNodeIds", typ: a("") },
      {
        json: "stationDescription",
        js: "stationDescription",
        typ: u(undefined, ""),
      },
      { json: "stationHeight", js: "stationHeight", typ: u(undefined, 3.14) },
      { json: "stationId", js: "stationId", typ: "" },
      { json: "stationName", js: "stationName", typ: u(undefined, "") },
      {
        json: "stationPosition",
        js: "stationPosition",
        typ: u(undefined, r("StationPosition")),
      },
    ],
    "any",
  ),
  StationPosition: o(
    [
      { json: "theta", js: "theta", typ: u(undefined, 3.14) },
      { json: "x", js: "x", typ: 3.14 },
      { json: "y", js: "y", typ: 3.14 },
    ],
    "any",
  ),
  MetaInformation: o(
    [
      { json: "creator", js: "creator", typ: "" },
      { json: "exportTimestamp", js: "exportTimestamp", typ: Date },
      { json: "lifVersion", js: "lifVersion", typ: "" },
      { json: "projectIdentification", js: "projectIdentification", typ: "" },
    ],
    "any",
  ),
};
