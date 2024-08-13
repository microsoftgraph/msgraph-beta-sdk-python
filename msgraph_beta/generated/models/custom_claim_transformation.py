from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contains_transformation import ContainsTransformation
    from .ends_with_transformation import EndsWithTransformation
    from .extract_alpha_transformation import ExtractAlphaTransformation
    from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation
    from .extract_number_transformation import ExtractNumberTransformation
    from .extract_transformation import ExtractTransformation
    from .if_empty_transformation import IfEmptyTransformation
    from .if_not_empty_transformation import IfNotEmptyTransformation
    from .join_transformation import JoinTransformation
    from .regex_replace_transformation import RegexReplaceTransformation
    from .starts_with_transformation import StartsWithTransformation
    from .substring_transformation import SubstringTransformation
    from .to_lowercase_transformation import ToLowercaseTransformation
    from .to_uppercase_transformation import ToUppercaseTransformation
    from .transformation_attribute import TransformationAttribute
    from .trim_transformation import TrimTransformation

@dataclass
class CustomClaimTransformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The input attribute that provides the source for the transformation. This parameter is required if it's the first or only transformation in the list of transformations to be applied. Subsequent transformations use the output of the prior transformation as input.
    input: Optional[TransformationAttribute] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaimTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaimTransformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.containsTransformation".casefold():
            from .contains_transformation import ContainsTransformation

            return ContainsTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endsWithTransformation".casefold():
            from .ends_with_transformation import EndsWithTransformation

            return EndsWithTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extractAlphaTransformation".casefold():
            from .extract_alpha_transformation import ExtractAlphaTransformation

            return ExtractAlphaTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extractMailPrefixTransformation".casefold():
            from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation

            return ExtractMailPrefixTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extractNumberTransformation".casefold():
            from .extract_number_transformation import ExtractNumberTransformation

            return ExtractNumberTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extractTransformation".casefold():
            from .extract_transformation import ExtractTransformation

            return ExtractTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ifEmptyTransformation".casefold():
            from .if_empty_transformation import IfEmptyTransformation

            return IfEmptyTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ifNotEmptyTransformation".casefold():
            from .if_not_empty_transformation import IfNotEmptyTransformation

            return IfNotEmptyTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.joinTransformation".casefold():
            from .join_transformation import JoinTransformation

            return JoinTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.regexReplaceTransformation".casefold():
            from .regex_replace_transformation import RegexReplaceTransformation

            return RegexReplaceTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startsWithTransformation".casefold():
            from .starts_with_transformation import StartsWithTransformation

            return StartsWithTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.substringTransformation".casefold():
            from .substring_transformation import SubstringTransformation

            return SubstringTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.toLowercaseTransformation".casefold():
            from .to_lowercase_transformation import ToLowercaseTransformation

            return ToLowercaseTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.toUppercaseTransformation".casefold():
            from .to_uppercase_transformation import ToUppercaseTransformation

            return ToUppercaseTransformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trimTransformation".casefold():
            from .trim_transformation import TrimTransformation

            return TrimTransformation()
        return CustomClaimTransformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .contains_transformation import ContainsTransformation
        from .ends_with_transformation import EndsWithTransformation
        from .extract_alpha_transformation import ExtractAlphaTransformation
        from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation
        from .extract_number_transformation import ExtractNumberTransformation
        from .extract_transformation import ExtractTransformation
        from .if_empty_transformation import IfEmptyTransformation
        from .if_not_empty_transformation import IfNotEmptyTransformation
        from .join_transformation import JoinTransformation
        from .regex_replace_transformation import RegexReplaceTransformation
        from .starts_with_transformation import StartsWithTransformation
        from .substring_transformation import SubstringTransformation
        from .to_lowercase_transformation import ToLowercaseTransformation
        from .to_uppercase_transformation import ToUppercaseTransformation
        from .transformation_attribute import TransformationAttribute
        from .trim_transformation import TrimTransformation

        from .contains_transformation import ContainsTransformation
        from .ends_with_transformation import EndsWithTransformation
        from .extract_alpha_transformation import ExtractAlphaTransformation
        from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation
        from .extract_number_transformation import ExtractNumberTransformation
        from .extract_transformation import ExtractTransformation
        from .if_empty_transformation import IfEmptyTransformation
        from .if_not_empty_transformation import IfNotEmptyTransformation
        from .join_transformation import JoinTransformation
        from .regex_replace_transformation import RegexReplaceTransformation
        from .starts_with_transformation import StartsWithTransformation
        from .substring_transformation import SubstringTransformation
        from .to_lowercase_transformation import ToLowercaseTransformation
        from .to_uppercase_transformation import ToUppercaseTransformation
        from .transformation_attribute import TransformationAttribute
        from .trim_transformation import TrimTransformation

        fields: Dict[str, Callable[[Any], None]] = {
            "input": lambda n : setattr(self, 'input', n.get_object_value(TransformationAttribute)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("input", self.input)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

