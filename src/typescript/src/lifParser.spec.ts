import { expect } from "chai";
import { describe, it } from "mocha";
import { LIFParser } from "./";
import { LIFLayoutCollection, BlockingType, RequirementType } from "./";

describe("LIFParser", () => {
  function assertLayoutCollection(layoutCollection: LIFLayoutCollection) {
    expect(layoutCollection).to.be.an("object");

    // Meta Information
    expect(layoutCollection.metaInformation.projectIdentification).to.equal(
      "Sample Project",
    );
    expect(layoutCollection.metaInformation.creator).to.equal("Sample Creator");
    expect(
      layoutCollection.metaInformation.exportTimestamp.toISOString(),
    ).to.equal("2069-07-21T00:37:33.000Z");
    expect(layoutCollection.metaInformation.lifVersion).to.equal("1.0.0");

    // Layouts
    expect(layoutCollection.layouts).to.have.lengthOf(2);

    // First Layout
    const layout1 = layoutCollection.layouts[0];
    expect(layout1.layoutId).to.equal("layout-001");
    expect(layout1.layoutName).to.equal("Main Layout");
    expect(layout1.layoutVersion).to.equal("1.1");
    expect(layout1.layoutLevelId).to.equal("level-001");
    expect(layout1.layoutDescription).to.equal("Primary layout for testing.");

    // First Layout Nodes
    expect(layout1.nodes).to.have.lengthOf(2);
    const node1 = layout1.nodes[0];
    expect(node1.nodeId).to.equal("node-001");
    expect(node1.nodeName).to.equal("Node A");
    expect(node1.nodeDescription).to.equal("Entrance node.");
    expect(node1.mapId).to.equal("map-001");
    expect(node1.nodePosition.x).to.equal(1000.0);
    expect(node1.nodePosition.y).to.equal(1500.0);

    // Vehicle Type Properties
    expect(node1.vehicleTypeNodeProperties).to.have.lengthOf(2);
    const vehicleType1 = node1.vehicleTypeNodeProperties[0];
    expect(vehicleType1.vehicleTypeId).to.equal("vehicle-001");
    expect(vehicleType1.theta).to.equal(90.0);

    // Vehicle Type Actions
    expect(vehicleType1.actions).to.not.be.null;
    const action1 = vehicleType1.actions![0];
    expect(action1.actionType).to.equal("move");
    expect(action1.actionDescription).to.equal("Move forward");
    expect(action1.requirementType).to.equal(RequirementType.Required);
    expect(action1.blockingType).to.equal(BlockingType.Hard);
    expect(action1.actionParameters).to.not.be.null;
    expect(action1.actionParameters![0].key).to.equal("speed");
    expect(action1.actionParameters![0].value).to.equal("fast");

    const vehicleType2 = node1.vehicleTypeNodeProperties[1];
    expect(vehicleType2.vehicleTypeId).to.equal("vehicle-002");

    // Layout Edges
    const edge1 = layout1.edges[0];
    expect(edge1.edgeId).to.equal("edge-001");
    expect(edge1.startNodeId).to.equal("node-001");
    expect(edge1.endNodeId).to.equal("node-002");

    // Layout Stations
    expect(layout1.stations).to.not.be.null;
    const station1 = layout1.stations![0];
    expect(station1.stationId).to.equal("station-001");
    expect(station1.interactionNodeIds).to.eql(["node-001", "node-002"]);
    expect(station1.stationPosition.x).to.equal(1000.0);
    expect(station1.stationPosition.y).to.equal(1000.0);

    // Second Layout
    const layout2 = layoutCollection.layouts[1];
    expect(layout2.layoutId).to.equal("layout-002");
    expect(layout2.nodes[0].nodeId).to.equal("node-003");
  }

  it("should throw an error for invalid JSON string", () => {
    const invalidJson = "{ invalid json }";
    expect(() => LIFParser.fromJson(invalidJson)).to.throw(SyntaxError);
  });

  it("should parse valid JSON string", () => {
    const validJson = `{
      "metaInformation": {
        "projectIdentification": "Sample Project",
        "creator": "Sample Creator",
        "exportTimestamp": "2069-07-21T00:37:33Z",
        "lifVersion": "1.0.0"
      },
      "layouts": [
        {
          "layoutId": "layout-001",
          "layoutName": "Main Layout",
          "layoutVersion": "1.1",
          "layoutLevelId": "level-001",
          "layoutDescription": "Primary layout for testing.",
          "nodes": [
            {
              "nodeId": "node-001",
              "nodeName": "Node A",
              "nodeDescription": "Entrance node.",
              "mapId": "map-001",
              "nodePosition": { "x": 1000.0, "y": 1500.0 },
              "vehicleTypeNodeProperties": [
                {
                  "vehicleTypeId": "vehicle-001",
                  "theta": 90.0,
                  "actions": [
                    {
                      "actionType": "move",
                      "actionDescription": "Move forward",
                      "requirementType": "REQUIRED",
                      "blockingType": "HARD",
                      "actionParameters": [
                        { "key": "speed", "value": "fast" },
                        { "key": "acceleration", "value": "medium" }
                      ]
                    }
                  ]
                },
                { "vehicleTypeId": "vehicle-002", "theta": 180.0, "actions": [] }
              ]
            },
            {
              "nodeId": "node-002",
              "nodeName": "Node B",
              "nodePosition": { "x": 2000.0, "y": 2500.0 },
              "vehicleTypeNodeProperties": [{ "vehicleTypeId": "vehicle-002" }]
            }
          ],
          "edges": [
            {
              "edgeId": "edge-001",
              "startNodeId": "node-001",
              "endNodeId": "node-002",
              "vehicleTypeEdgeProperties": [
                {
                  "vehicleTypeId": "vehicle-001",
                  "vehicleOrientation": 0.0,
                  "orientationType": "TANGENTIAL",
                  "rotationAllowed": true,
                  "maxSpeed": 1.5,
                  "maxRotationSpeed": 0.5,
                  "loadRestriction": {
                    "unloaded": true,
                    "loaded": false,
                    "loadSetNames": ["set1", "set2"]
                  }
                }
              ]
            }
          ],
          "stations": [
            {
              "stationId": "station-001",
              "interactionNodeIds": ["node-001", "node-002"],
              "stationName": "Station A",
              "stationDescription": "Primary loading station.",
              "stationPosition": { "x": 1000.0, "y": 1000.0, "theta": 0.0 }
            }
          ]
        },
        {
          "layoutId": "layout-002",
          "layoutName": "Secondary Layout",
          "layoutVersion": "1.0",
          "layoutLevelId": "level-002",
          "nodes": [
            {
              "nodeId": "node-003",
              "nodePosition": { "x": 3000.0, "y": 3500.0 },
              "vehicleTypeNodeProperties": [{ "vehicleTypeId": "vehicle-003", "theta": 270.0 }]
            }
          ],
          "edges": [],
          "stations": []
        }
      ]
    }`;
    const layoutCollection = LIFParser.fromJson(validJson);
    assertLayoutCollection(layoutCollection);
  });
});
