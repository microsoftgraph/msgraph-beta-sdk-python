from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_format_reference_value import FileFormatReferenceValue
    from .identifier_type_reference_value import IdentifierTypeReferenceValue
    from .reference_definition import ReferenceDefinition
    from .role_reference_value import RoleReferenceValue
    from .section_role_reference_value import SectionRoleReferenceValue
    from .user_match_target_reference_value import UserMatchTargetReferenceValue
    from .year_reference_value import YearReferenceValue

@dataclass
class ReferenceValue(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The code of the desired referenceDefinition entry.
    code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The value property
    value: Optional[ReferenceDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReferenceValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileFormatReferenceValue".casefold():
            from .file_format_reference_value import FileFormatReferenceValue

            return FileFormatReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.identifierTypeReferenceValue".casefold():
            from .identifier_type_reference_value import IdentifierTypeReferenceValue

            return IdentifierTypeReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.roleReferenceValue".casefold():
            from .role_reference_value import RoleReferenceValue

            return RoleReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.sectionRoleReferenceValue".casefold():
            from .section_role_reference_value import SectionRoleReferenceValue

            return SectionRoleReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.userMatchTargetReferenceValue".casefold():
            from .user_match_target_reference_value import UserMatchTargetReferenceValue

            return UserMatchTargetReferenceValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.yearReferenceValue".casefold():
            from .year_reference_value import YearReferenceValue

            return YearReferenceValue()
        return ReferenceValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_format_reference_value import FileFormatReferenceValue
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .reference_definition import ReferenceDefinition
        from .role_reference_value import RoleReferenceValue
        from .section_role_reference_value import SectionRoleReferenceValue
        from .user_match_target_reference_value import UserMatchTargetReferenceValue
        from .year_reference_value import YearReferenceValue

        from .file_format_reference_value import FileFormatReferenceValue
        from .identifier_type_reference_value import IdentifierTypeReferenceValue
        from .reference_definition import ReferenceDefinition
        from .role_reference_value import RoleReferenceValue
        from .section_role_reference_value import SectionRoleReferenceValue
        from .user_match_target_reference_value import UserMatchTargetReferenceValue
        from .year_reference_value import YearReferenceValue

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(ReferenceDefinition)),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

