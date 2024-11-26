import {
    CSharpRenderer,
    CSharpTargetLanguage,
    Sourcelike,
    type Type,
    RenderContext,
    getOptionValues,
    cSharpOptions,
    SystemTextJsonCSharpRenderer
} from "quicktype-core";

export class OptionalAwareCSharpTargetLanguage extends CSharpTargetLanguage {
    protected makeRenderer(renderContext: RenderContext, untypedOptionValues: { [name: string]: any }): CSharpRenderer {
       
        return new OptionalAwareCSharpRenderer(this, renderContext, getOptionValues(cSharpOptions, untypedOptionValues));
    }
}

class OptionalAwareCSharpRenderer extends SystemTextJsonCSharpRenderer {

    /**
     * Render all nullables cstype using "?"
     * In the original implementation only "value types" are rendered as "<Type>?". 
     * This leads to problems when using the schema with ASP.NET where all non nullable fields are seen as required.
     * @param t
     * @param follow
     * @param withIssues
     * @protected
     */
    protected nullableCSType(t: Type, follow?: (t: Type) => Type, withIssues?: boolean): Sourcelike {
        const csType = this.csType(t, follow, withIssues);
        return [csType, "?"];
    }
}