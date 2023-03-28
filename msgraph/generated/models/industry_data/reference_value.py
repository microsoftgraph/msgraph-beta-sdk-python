from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identifier_type_reference_value, reference_definition, role_reference_value, user_match_target_reference_value, year_reference_value

class ReferenceValue(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new referenceValue and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The code of the desired referenceDefinition entry.
        self._code: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The value property
        self._value: Optional[reference_definition.ReferenceDefinition] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code of the desired referenceDefinition entry.
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code of the desired referenceDefinition entry.
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReferenceValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReferenceValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.identifierTypeReferenceValue":
                from . import identifier_type_reference_value

                return identifier_type_reference_value.IdentifierTypeReferenceValue()
            if mapping_value == "#microsoft.graph.industryData.roleReferenceValue":
                from . import role_reference_value

                return role_reference_value.RoleReferenceValue()
            if mapping_value == "#microsoft.graph.industryData.userMatchTargetReferenceValue":
                from . import user_match_target_reference_value

                return user_match_target_reference_value.UserMatchTargetReferenceValue()
            if mapping_value == "#microsoft.graph.industryData.yearReferenceValue":
                from . import year_reference_value

                return year_reference_value.YearReferenceValue()
        return ReferenceValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identifier_type_reference_value, reference_definition, role_reference_value, user_match_target_reference_value, year_reference_value

        fields: Dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(reference_definition.ReferenceDefinition)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("code", self.code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[reference_definition.ReferenceDefinition]:
        """
        Gets the value property value. The value property
        Returns: Optional[reference_definition.ReferenceDefinition]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[reference_definition.ReferenceDefinition] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

