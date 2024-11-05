import { execSync } from "child_process";
import * as fs from "fs";
import * as path from "path";
import * as dotenv from "dotenv";
import {LanguageConfig} from "../config/config";

// Load environment variables from .env file
dotenv.config();

async function publishPyPi(config: LanguageConfig): Promise<void> {
    if(config.language != "python") {
        console.error("Only a python can be published to PyPi");
        process.exit(1);
    }

    if (!config.publish) {
        console.error("Publish configuration is missing in LanguageConfig.");
        process.exit(1);
    }

    const { packageName, packageDirectory, packageVersion } = config.publish;

    // Get the PyPI API token from environment variables
    const pypiApiKey = process.env.PYPI_API_KEY;

    // Validate configuration fields and API token
    if (!packageName || !packageDirectory || !pypiApiKey) {
      console.error("Missing required configuration fields or API token.");
      process.exit(1);
    }

    // Construct the path to the Python package files
    const tgzFileName = `${packageName}-${packageVersion}.tar.gz`
    const whlFileName = `${packageName}-${packageVersion}-py3-none-any.whl`
    const packagePath = path.resolve(path.join(config.outputDirectory, packageDirectory));
    const packageFiles = fs.readdirSync(packagePath).filter(file => file.endsWith(tgzFileName) || file.endsWith(whlFileName));

    if (packageFiles.length === 0) {
      console.error(`No package files found in directory: ${packagePath}`);
      process.exit(1);
    }

    try {
      // Run Twine to publish the package
      console.log(`Publishing ${packageName} to PyPI...`);
      execSync(`python -m twine upload ${packagePath}/${tgzFileName} ${packagePath}/${whlFileName} -u __token__ -p ${pypiApiKey}`, {
        stdio: "inherit",
      });
      console.log("Package published successfully!");
    } catch (error) {
      console.error("Error publishing package to PyPI:", (error as Error).message);
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

publishPyPi(config);
