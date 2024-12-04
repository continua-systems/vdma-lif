import { Convert, type LIFLayoutCollection } from "./lifModels";

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
}
