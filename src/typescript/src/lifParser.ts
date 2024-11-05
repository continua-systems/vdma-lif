import fs from "fs";
import { Convert, LIFLayoutCollection } from "./lifModels";

export class LIFParser {
  static fromJson(jsonData: string): LIFLayoutCollection | null {
    /**
     * Parses JSON string data into a LIFLayoutCollection object.
     *
     * @param jsonData - JSON string representing the LIF schema.
     * @returns Parsed LIFLayoutCollection object.
     */
    return Convert.toLIFLayoutCollection(jsonData);
  }

  static fromFile(filePath: string): LIFLayoutCollection | null {
    /**
     * Reads a JSON file and parses it into a LIFLayoutCollection object.
     *
     * @param filePath - Path to the JSON file representing the LIF schema.
     * @returns Parsed LIFLayoutCollection object.
     */

    const data = fs.readFileSync(filePath, "utf-8");
    return LIFParser.fromJson(data);
  }

  static toJson(
    layoutCollection: LIFLayoutCollection,
    indent?: number,
  ): string {
    /**
     * Serializes layoutCollection into JSON string.
     *
     * @param layoutCollection - LIF layoutCollection to be serialized.
     * @param indent - If provided, formats JSON with the specified indent level.
     * @returns Serialized JSON string.
     */
    return JSON.stringify(layoutCollection, null, indent);
  }

  static toFile(
    layoutCollection: LIFLayoutCollection,
    filePath: string,
    indent?: number,
  ): void {
    /**
     * Serializes layoutCollection into JSON string and saves it to file.
     *
     * @param layoutCollection - LIF layoutCollection to be serialized.
     * @param filePath - File path where the layoutCollection will be stored.
     * @param indent - If provided, formats JSON with the specified indent level.
     */
    try {
      const jsonString = LIFParser.toJson(layoutCollection, indent);
      fs.writeFileSync(filePath, jsonString, "utf-8");
    } catch (error) {
      console.error("Failed to write to file:", error);
    }
  }
}
