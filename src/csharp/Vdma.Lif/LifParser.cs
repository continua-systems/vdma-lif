using System.Text.Json;

namespace Vdma.Lif;

public static class LifJsonParser
{
    /// <summary>
    ///     Reads a LIF JSON file from the specified path and deserializes its content into
    ///     an instance of <see cref="LifLayoutCollection" />.
    /// </summary>
    /// <param name="jsonFilePath">The file path to the JSON file containing the data to be parsed.</param>
    /// <returns>
    ///     An instance of <see cref="LifLayoutCollection" /> representing the deserialized JSON data, or <c>null</c> if the
    ///     deserialization fails.
    /// </returns>
    /// <exception cref="ArgumentException">
    ///     Thrown when <paramref name="jsonFilePath" /> is <c>null</c>, empty, or consists only of whitespace.
    /// </exception>
    /// <exception cref="PathTooLongException">
    ///     Thrown when the specified path, file name, or combined path and file name exceed the system-defined maximum length.
    /// </exception>
    /// <exception cref="DirectoryNotFoundException">
    ///     Thrown when the specified path is invalid, such as being on an unmapped drive.
    /// </exception>
    /// <exception cref="IOException">
    ///     Thrown when an I/O error occurs while opening the file.
    /// </exception>
    /// <exception cref="UnauthorizedAccessException">
    ///     Thrown when <paramref name="jsonFilePath" /> specifies a read-only file, the operation is not supported on the
    ///     current platform,
    ///     or the caller does not have the required permission to access the file or directory.
    /// </exception>
    /// <exception cref="FileNotFoundException">
    ///     Thrown when the file specified in <paramref name="jsonFilePath" /> is not found.
    /// </exception>
    /// <exception cref="NotSupportedException">
    ///     Thrown when <paramref name="jsonFilePath" /> is in an invalid format.
    /// </exception>
    /// <exception cref="SecurityException">
    ///     Thrown when the caller does not have the required permission to access the file specified in
    ///     <paramref name="jsonFilePath" />.
    /// </exception>
    public static LifLayoutCollection? FromFile(string jsonFilePath)
    {
        var jsonData = File.ReadAllText(jsonFilePath);
        return FromJson(jsonData);
    }

    /// <summary>
    ///     Deserializes a JSON string into an instance of <see cref="LifLayoutCollection" />.
    /// </summary>
    /// <param name="jsonData">A JSON string representing the data to be deserialized.</param>
    /// <returns>
    ///     An instance of <see cref="LifLayoutCollection" /> representing the deserialized JSON data, or <c>null</c> if the
    ///     deserialization fails.
    /// </returns>
    /// <exception cref="ArgumentNullException">
    ///     Thrown when <paramref name="jsonData" /> is <c>null</c>.
    /// </exception>
    /// <exception cref="JsonException">
    ///     Thrown when the JSON data is invalid, incompatible with the <see cref="LifLayoutCollection" /> type,
    ///     or contains additional data beyond a single JSON value.
    /// </exception>
    /// <exception cref="NotSupportedException">
    ///     Thrown when there is no compatible <see cref="JsonConverter" /> for the <see cref="LifLayoutCollection" /> type
    ///     or one of its serializable members.
    /// </exception>
    /// <exception cref="InvalidOperationException">
    ///     Thrown when the <c>GetTypeInfo(Type)</c> method of the provided serialization context returns <c>null</c>
    ///     for the <see cref="LifLayoutCollection" /> type to convert.
    /// </exception>
    public static LifLayoutCollection? FromJson(string jsonData)
    {
        var options = new JsonSerializerOptions(Converter.Settings)
        {
            PropertyNameCaseInsensitive = true
        };
        var layoutCollection = JsonSerializer.Deserialize<LifLayoutCollection>(jsonData, options);

        return layoutCollection;
    }

    /// <summary>
    ///     Serialize LIF layout collection into JSON string
    /// </summary>
    /// <param name="layoutCollection">LIF Layout Collection</param>
    /// <param name="indented">Indicates whether JSON should use pretty printing</param>
    /// <returns>Serialized json string</returns>
    public static string ToJson(this LifLayoutCollection layoutCollection, bool indented = false)
    {
        var options = new JsonSerializerOptions(Converter.Settings)
        {
            WriteIndented = indented
        };
        return JsonSerializer.Serialize(layoutCollection, options);
    }

    /// <summary>
    ///     Save LIF layout collection into a json serialized file
    /// </summary>
    /// <param name="layoutCollection">LIF Layout collection</param>
    /// <param name="filePath">file path</param>
    /// <param name="indented">Indicates whether JSON should use pretty printing</param>
    public static void ToFile(this LifLayoutCollection layoutCollection, string filePath, bool indented = false)
    {
        File.WriteAllText(filePath, layoutCollection.ToJson(indented));
    }
}