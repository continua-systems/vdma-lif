import { quicktype, InputData, JSONSchemaInput, FetchingJSONSchemaStore } from 'quicktype-core';
import * as fs from 'fs';
import * as path from 'path';
import { execSync } from 'child_process';
import { LanguageConfig } from '../config/config';

// Define the path to the input schema
const inputSchemaFile = 'schema/lif-schema.json';
const rootClassName = "LifLayoutCollection"

// Get config file path from command-line arguments
const configFilePath = process.argv[2];

if (!configFilePath) {
    console.error("Please provide a path to the configuration file (e.g., 'ts-node script/generateCode.ts src/config/csharp.json').");
    process.exit(1);
}

// Load configuration from specified file
const config: LanguageConfig = JSON.parse(fs.readFileSync(configFilePath, 'utf-8'));

// Ensure output directory exists
if (config.outputDirectory) {
    fs.mkdirSync(config.outputDirectory, { recursive: true });
}

// Define full output path by combining the directory and file name
const outputFilePath = path.join(config.outputDirectory, config.outputFile);

// Function to generate code from JSON schema for a specific language
async function generateCodeFromSchema(config: LanguageConfig): Promise<void> {
    try {
        // Read the JSON schema file
        const schema = fs.readFileSync(inputSchemaFile, 'utf-8');

        // Set up JSON schema input using FetchingJSONSchemaStore
        const schemaInput = new JSONSchemaInput(new FetchingJSONSchemaStore());
        await schemaInput.addSource({
            name: rootClassName,
            schema: schema,
        });

        // Prepare the input data for quicktype
        const inputData = new InputData();
        inputData.addInput(schemaInput);

        // Define renderer options based on the config
        const rendererOptions: { [key: string]: string } = {
            "alphabetize-properties": "true",
            ...config.renderOptions,
        };

        // Generate code for the specified language
        const { lines } = await quicktype({
            inputData,
            lang: config.language,
            rendererOptions,
        });

        // Combine any custom prepend text with generated code
        const generatedCode = `${config.prepend || ''}\n${lines.join('\n')}`;

        // Write the final output to the specified file in the output directory
        fs.writeFileSync(outputFilePath, generatedCode, 'utf-8');

        console.log(`${outputFilePath} has been successfully generated for ${config.language}.`);

        // Execute cleanupCommand if specified
        if (config.cleanupCommand) {
            console.log(`Running cleanup command in ${config.outputDirectory}: ${config.cleanupCommand}`);
            execSync(config.cleanupCommand, { cwd: config.outputDirectory, stdio: 'inherit' });
            console.log(`Cleanup command executed successfully.`);
        }

        // Execute Tests if specified
        if (config.testCommand) {
            console.log(`Running tests in ${config.outputDirectory}: ${config.testCommand}`);
            execSync(config.testCommand, { cwd: config.outputDirectory, stdio: 'inherit' });
            console.log(`Tests command executed successfully.`);
        }

        // Execute Tests if specified
        if (config.buildCommand) {
            console.log(`Building in ${config.outputDirectory}: ${config.buildCommand}`);
            execSync(config.buildCommand, { cwd: config.outputDirectory, stdio: 'inherit' });
            console.log(`Build command executed successfully.`);
        }
    } catch (error) {
        console.error(`Error generating code for ${config.language}:`, error);
    }
}

// Run the function with the loaded configuration
generateCodeFromSchema(config);
