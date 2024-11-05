import json
from typing import Optional
from .models import LIFSchema, lif_schema_from_dict


class LIFParser:
    @staticmethod
    def from_json(json_data: str) -> Optional[LIFSchema]:
        """
        Parses JSON string data into a LIFSchema object.

        :param json_data:  JSON string representing the LIF schema.
        :return: Parsed LIFSchema object.
        """

        data = json.loads(json_data)
        return lif_schema_from_dict(data)

    @staticmethod
    def from_file(file_path: str) -> Optional[LIFSchema]:
        """
        Reads a JSON file and parses it into a LIFSchema object.

        :param file_path: Path to the JSON file representing the LIF schema.
        :return: Parsed LIFSchema object.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return lif_schema_from_dict(data)

    @staticmethod
    def to_json(schema: LIFSchema, indent=None) -> str:
        """
        Serialize schema into json string

        :param schema: LIF schema to be serialized
        :param indent: If is a non-negative integer, then JSON array elements and
                object members will be pretty-printed with that indent level. An indent
                level of 0 will only insert newlines. ``None`` is the most compact
                representation.
        :return: Serialized json str
        """
        return json.dumps(schema.to_dict(), indent=indent)

    @staticmethod
    def to_file(schema: LIFSchema, file_path: str, indent=None):
        """
        Serialize schema into json string and store in file_path

        :param file_path: file path where the schema will be stored
        :param schema: LIF schema to be serialized
        :param indent: If is a non-negative integer, then JSON array elements and
                object members will be pretty-printed with that indent level. An indent
                level of 0 will only insert newlines. ``None`` is the most compact
                representation.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            return file.write(json.dumps(schema.to_dict(), indent=indent))
