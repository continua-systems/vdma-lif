import fs from "fs";
import { Convert, LIFSchema } from "./lifModels";

export class LifParser {
  static fromJson(jsonData: string): LIFSchema | null {
    /**
     * Parses JSON string data into a LIFSchema object.
     *
     * @param jsonData - JSON string representing the LIF schema.
     * @returns Parsed LIFSchema object.
     */
    return Convert.toLIFSchema(jsonData);
  }

  static fromFile(filePath: string): LIFSchema | null {
    /**
     * Reads a JSON file and parses it into a LIFSchema object.
     *
     * @param filePath - Path to the JSON file representing the LIF schema.
     * @returns Parsed LIFSchema object.
     */

    const data = fs.readFileSync(filePath, "utf-8");
    return LifParser.fromJson(data);
  }

  static toJson(schema: LIFSchema, indent?: number): string {
    /**
     * Serializes schema into JSON string.
     *
     * @param schema - LIF schema to be serialized.
     * @param indent - If provided, formats JSON with the specified indent level.
     * @returns Serialized JSON string.
     */
    return JSON.stringify(schema, null, indent);
  }

  static toFile(schema: LIFSchema, filePath: string, indent?: number): void {
    /**
     * Serializes schema into JSON string and saves it to file.
     *
     * @param schema - LIF schema to be serialized.
     * @param filePath - File path where the schema will be stored.
     * @param indent - If provided, formats JSON with the specified indent level.
     */
    try {
      const jsonString = LifParser.toJson(schema, indent);
      fs.writeFileSync(filePath, jsonString, "utf-8");
    } catch (error) {
      console.error("Failed to write to file:", error);
    }
  }
}
