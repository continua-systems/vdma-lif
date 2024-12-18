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
import {ClassProperty, ClassType} from "quicktype-core/dist/Type";
import type {Name} from "quicktype-core/dist/Naming";

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

    /**
     * Adds JsonRequired attribute when field is not optional
     * @param property
     * @param _name
     * @param _c
     * @param jsonName
     * @protected
     */
    protected attributesForProperty(property: ClassProperty, _name: Name, _c: ClassType, jsonName: string): Sourcelike[] | undefined {
        let attributes: Sourcelike[] = [];
        if(!property.isOptional) {
            attributes.push(['[JsonRequired]'])
        }
        attributes.push(super.attributesForProperty(property, _name, _c, jsonName));
        if(attributes.length > 0) {
            return attributes;
        }
        return undefined;
    }
}