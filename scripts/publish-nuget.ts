import { execSync } from "child_process";
import * as fs from "fs";
import * as path from "path";
import * as dotenv from "dotenv";
import {LanguageConfig} from "../config/config";

// Load environment variables from .env file
dotenv.config();

// Function to publish the NuGet package
async function publishNuGet(config: LanguageConfig): Promise<void> {
    if(config.language != "csharp") {
        console.error("Only a csharp can be published to NuGet");
        process.exit(1);
    }

    if (!config.publish) {
        console.error("Publish configuration is missing in LanguageConfig.");
        process.exit(1);
    }

    const { packageName, packageDirectory, packageVersion } = config.publish;
    const apiKey = process.env.NUGET_API_KEY;

    // Validate configuration fields
    if (!packageName || !packageDirectory || !packageVersion || !apiKey) {
        console.error("Missing required configuration fields or API key.");
        process.exit(1);
    }

    const packageDirectoryFull = path.join(config.outputDirectory, packageDirectory);

    // Construct the path to the .nupkg file
    const packageFilePath = path.resolve(packageDirectoryFull, `${packageName}.${packageVersion}.nupkg`);

    if (!fs.existsSync(packageFilePath)) {
        console.error(`Package file not found: ${packageFilePath}`);
        process.exit(1);
    }

    const nugetSource = "https://api.nuget.org/v3/index.json"; // Default NuGet source, modify if needed

    // Push the package to NuGet
    try {
        console.log(`Pushing ${packageFilePath} to NuGet...`);
        execSync(
            `dotnet nuget push ${packageFilePath} --api-key ${apiKey} --source ${nugetSource}`,
            { stdio: "inherit" }
        );
        console.log("Package pushed successfully!");
    } catch (error) {
        console.error("Error pushing package to NuGet:", (error as Error).message);
        process.exit(1);
    }
}

// Get config file path from command-line arguments
const configFilePath = process.argv[2];

if (!configFilePath) {
    console.error("Please provide a path to the configuration file.");
    process.exit(1);
}

// Load configuration from specified file
const config: LanguageConfig = JSON.parse(fs.readFileSync(configFilePath, 'utf-8'));

// Run the publish function with example configuration
publishNuGet(config);
