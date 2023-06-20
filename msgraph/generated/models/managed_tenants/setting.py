from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_parameter_value_type

@dataclass
class Setting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The display name for the setting. Required. Read-only.
    display_name: Optional[str] = None
    # The value for the setting serialized as string of JSON. Required. Read-only.
    json_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A flag indicating whether the setting can be override existing configurations when applied. Required. Read-only.
    overwrite_allowed: Optional[bool] = None
    # The settingId property
    setting_id: Optional[str] = None
    # The valueType property
    value_type: Optional[management_parameter_value_type.ManagementParameterValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Setting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Setting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Setting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_parameter_value_type

        from . import management_parameter_value_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "jsonValue": lambda n : setattr(self, 'json_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overwriteAllowed": lambda n : setattr(self, 'overwrite_allowed', n.get_bool_value()),
            "settingId": lambda n : setattr(self, 'setting_id', n.get_str_value()),
            "valueType": lambda n : setattr(self, 'value_type', n.get_enum_value(management_parameter_value_type.ManagementParameterValueType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("jsonValue", self.json_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("overwriteAllowed", self.overwrite_allowed)
        writer.write_str_value("settingId", self.setting_id)
        writer.write_enum_value("valueType", self.value_type)
        writer.write_additional_data_value(self.additional_data)
    

