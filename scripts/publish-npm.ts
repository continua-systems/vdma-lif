import { execSync } from "child_process";
import * as fs from "fs";
import * as dotenv from "dotenv";
import {LanguageConfig} from "../config/config";

// Load environment variables from .env file
dotenv.config();

// Function to publish the NuGet package
async function publishNpm(config: LanguageConfig): Promise<void> {
    if(config.language != "typescript") {
        console.error("Only a typescript can be published to NPM");
        process.exit(1);
    }

    const apiKey = process.env.NPM_API_KEY;

    // Validate configuration fields
    if (!config.outputDirectory || !apiKey) {
        console.error("Missing required configuration fields or API key.");
        process.exit(1);
    }

    // Push the package to NPM
    try {
        console.log(`Pushing to NPM...`);
        execSync(
        `npm set "//registry.npmjs.org/:_authToken=${apiKey}"`,
            { stdio: "inherit", cwd: config.outputDirectory },
        );
        execSync(
            `npm publish`,
            { stdio: "inherit", cwd: config.outputDirectory }
        );
        console.log("Package pushed successfully!");
    } catch (error) {
        console.error("Error pushing package to NPM:", (error as Error).message);
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
publishNpm(config);
