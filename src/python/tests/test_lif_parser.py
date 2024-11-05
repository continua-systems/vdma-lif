import tempfile
import unittest
from vdma_lif.parser import LIFParser
from vdma_lif.models import LIFLayoutCollection
import json
from pathlib import Path


class TestLIFParser(unittest.TestCase):

    @property
    def sample_file(self) -> str:
        # Path to the example JSON file for testing
        path = Path(__file__).parent / '../../../examples/example.lif.json'
        return str(path.resolve())

    def test_from_file_valid_json(self):
        # Test parsing a valid JSON file
        layout_collection = LIFParser.from_file(self.sample_file)
        self.assert_layout_collection(layout_collection)


    def test_from_string_invalid_json(self):
        # Test parsing invalid JSON string
        invalid_json = '{ invalid json }'
        with self.assertRaises(json.JSONDecodeError):
            LIFParser.from_json(invalid_json)

    def test_from_file_nonexistent_file(self):
        # Test parsing a non-existent file
        non_existent_file = "nonexistent_file.json"
        with self.assertRaises(FileNotFoundError):
            LIFParser.from_file(non_existent_file)

    def test_to_file_valid_json(self):
        # Test parsing a valid JSON file
        layout_collection = LIFParser.from_file(self.sample_file)
        self.assert_layout_collection(layout_collection)

        with tempfile.NamedTemporaryFile(delete_on_close=False) as fp:
            LIFParser.to_file(layout_collection, fp.name)
            layout_collection_from_file = LIFParser.from_file(fp.name)
            self.assert_layout_collection(layout_collection_from_file)


    def assert_layout_collection(self, layout_collection: LIFLayoutCollection):
        self.assertIsInstance(layout_collection, LIFLayoutCollection)

        # Check Meta Information
        self.assertEqual(
            layout_collection.meta_information.project_identification, "Sample Project")
        self.assertEqual(layout_collection.meta_information.creator, "Sample Creator")
        self.assertEqual(layout_collection.meta_information.export_timestamp.isoformat(
        ), "2069-07-21T00:37:33+00:00")
        self.assertEqual(layout_collection.meta_information.lif_version, "1.0.0")

        # Check Layouts
        self.assertEqual(len(layout_collection.layouts), 2)

        # First Layout
        layout1 = layout_collection.layouts[0]
        self.assertEqual(layout1.layout_id, "layout-001")
        self.assertEqual(layout1.layout_name, "Main Layout")
        self.assertEqual(layout1.layout_version, "1.1")
        self.assertEqual(layout1.layout_level_id, "level-001")
        self.assertEqual(layout1.layout_description,
                         "Primary layout for testing.")

        # First Layout Nodes
        self.assertEqual(len(layout1.nodes), 2)

        node1 = layout1.nodes[0]
        self.assertEqual(node1.node_id, "node-001")
        self.assertEqual(node1.node_name, "Node A")
        self.assertEqual(node1.node_description, "Entrance node.")
        self.assertEqual(node1.map_id, "map-001")
        self.assertEqual(node1.node_position.x, 1000.0)
        self.assertEqual(node1.node_position.y, 1500.0)

        # Node Vehicle Type Properties
        self.assertEqual(len(node1.vehicle_type_node_properties), 2)
        vehicle_type1 = node1.vehicle_type_node_properties[0]
        self.assertEqual(vehicle_type1.vehicle_type_id, "vehicle-001")
        self.assertEqual(vehicle_type1.theta, 90.0)

        # Actions for Vehicle Type 1
        self.assertEqual(len(vehicle_type1.actions), 1)
        action1 = vehicle_type1.actions[0]
        self.assertEqual(action1.action_type, "move")
        self.assertEqual(action1.action_description, "Move forward")
        self.assertTrue(action1.required)
        self.assertEqual(action1.blocking_type, "HARD")
        self.assertEqual(len(action1.action_parameters), 2)
        self.assertEqual(action1.action_parameters[0].key, "speed")
        self.assertEqual(action1.action_parameters[0].value, "fast")

        # Edges
        self.assertEqual(len(layout1.edges), 2)
        edge1 = layout1.edges[0]
        self.assertEqual(edge1.edge_id, "edge-001")
        self.assertEqual(edge1.start_node_id, "node-001")
        self.assertEqual(edge1.end_node_id, "node-002")

        # Vehicle Type Edge Properties for Edge 1
        self.assertEqual(len(edge1.vehicle_type_edge_properties), 1)
        edge_vehicle_type1 = edge1.vehicle_type_edge_properties[0]
        self.assertEqual(edge_vehicle_type1.vehicle_type_id, "vehicle-001")
        self.assertEqual(edge_vehicle_type1.vehicle_orientation, 0.0)
        self.assertEqual(edge_vehicle_type1.orientation_type, "TANGENTIAL")
        self.assertTrue(edge_vehicle_type1.rotation_allowed)
        self.assertEqual(edge_vehicle_type1.max_speed, 1.5)
        self.assertEqual(edge_vehicle_type1.max_rotation_speed, 0.5)
        self.assertTrue(edge_vehicle_type1.load_restriction.unloaded)
        self.assertFalse(edge_vehicle_type1.load_restriction.loaded)
        self.assertEqual(
            edge_vehicle_type1.load_restriction.load_set_names, ["set1", "set2"])

        # Stations
        self.assertEqual(len(layout1.stations), 2)
        station1 = layout1.stations[0]
        self.assertEqual(station1.station_id, "station-001")
        self.assertEqual(station1.interaction_node_ids,
                         ["node-001", "node-002"])
        self.assertEqual(station1.station_name, "Station A")
        self.assertEqual(station1.station_description,
                         "Primary loading station.")
        self.assertEqual(station1.station_position.x, 1000.0)
        self.assertEqual(station1.station_position.y, 1000.0)
        self.assertEqual(station1.station_position.theta, 0.0)

        # Second Layout
        layout2 = layout_collection.layouts[1]
        self.assertEqual(layout2.layout_id, "layout-002")
        self.assertEqual(layout2.layout_name, "Secondary Layout")
        self.assertEqual(layout2.layout_version, "1.0")
        self.assertEqual(layout2.layout_level_id, "level-002")

        # Second Layout Nodes
        self.assertEqual(len(layout2.nodes), 1)
        node3 = layout2.nodes[0]
        self.assertEqual(node3.node_id, "node-003")
        self.assertEqual(node3.node_position.x, 3000.0)
        self.assertEqual(node3.node_position.y, 3500.0)
        self.assertEqual(len(node3.vehicle_type_node_properties), 1)
        self.assertEqual(
            node3.vehicle_type_node_properties[0].vehicle_type_id, "vehicle-003")
        self.assertEqual(node3.vehicle_type_node_properties[0].theta, 270.0)

        # No edges and stations in the second layout
        self.assertEqual(len(layout2.edges), 0)
        self.assertEqual(len(layout2.stations), 0)


if __name__ == '__main__':
    unittest.main()
