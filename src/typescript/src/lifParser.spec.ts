import fs from "fs";
import path from "path";
import { expect } from "chai";
import { describe, it } from "mocha";
import { LIFParser } from "./";
import { LIFLayoutCollection } from "./";

describe("LIFParser", () => {
  const sampleFile = path.resolve(
    __dirname,
    "../../../examples/example.lif.json",
  );

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
    expect(action1.required).to.be.true;
    expect(action1.blockingType).to.equal("HARD");
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

  it("should parse a valid JSON file", () => {
    const layoutCollection = LIFParser.fromFile(sampleFile);
    expect(layoutCollection).to.not.be.null;
    if (layoutCollection) assertLayoutCollection(layoutCollection);
  });

  it("should throw an error for invalid JSON string", () => {
    const invalidJson = "{ invalid json }";
    expect(() => LIFParser.fromJson(invalidJson)).to.throw(SyntaxError);
  });

  it("should throw an error for a nonexistent file", () => {
    const nonExistentFile = "nonexistent_file.json";
    expect(() => LIFParser.fromFile(nonExistentFile)).to.throw(Error);
  });

  it("should write and read lif layouts to/from a file", () => {
    const layoutCollection = LIFParser.fromFile(sampleFile);
    expect(layoutCollection).to.not.be.null;

    const tempFile = path.resolve(__dirname, "temp_lif.json");
    if (layoutCollection) {
      LIFParser.toFile(layoutCollection, tempFile);
      const layoutCollectionFromFile = LIFParser.fromFile(tempFile);
      expect(layoutCollectionFromFile).to.not.be.null;
      if (layoutCollectionFromFile)
        assertLayoutCollection(layoutCollectionFromFile);

      // Cleanup
      fs.unlinkSync(tempFile);
    }
  });
});
