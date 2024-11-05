import {RendererOptions} from "quicktype-core/dist/Run";


export interface LanguageConfig {
    language: string;
    outputFile: string;
    outputDirectory: string;
    prepend?: string;
    renderOptions?: Partial<RendererOptions>;
    cleanupCommand?: string;
    testCommand?: string;
    buildCommand?: string;
    publish?: PublishConfig
}

interface PublishConfig {
    packageName: string;
    packageVersion: string;
    packageDirectory: string;
}