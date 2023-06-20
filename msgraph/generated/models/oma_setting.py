from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import oma_setting_base64, oma_setting_boolean, oma_setting_date_time, oma_setting_floating_point, oma_setting_integer, oma_setting_string, oma_setting_string_xml

@dataclass
class OmaSetting(AdditionalDataHolder, Parsable):
    """
    OMA Settings definition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Description.
    description: Optional[str] = None
    # Display Name.
    display_name: Optional[str] = None
    # Indicates whether the value field is encrypted. This property is read-only.
    is_encrypted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OMA.
    oma_uri: Optional[str] = None
    # ReferenceId for looking up secret for decryption. This property is read-only.
    secret_reference_value_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingBase64".casefold():
            from . import oma_setting_base64

            return oma_setting_base64.OmaSettingBase64()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingBoolean".casefold():
            from . import oma_setting_boolean

            return oma_setting_boolean.OmaSettingBoolean()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingDateTime".casefold():
            from . import oma_setting_date_time

            return oma_setting_date_time.OmaSettingDateTime()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingFloatingPoint".casefold():
            from . import oma_setting_floating_point

            return oma_setting_floating_point.OmaSettingFloatingPoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingInteger".casefold():
            from . import oma_setting_integer

            return oma_setting_integer.OmaSettingInteger()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingString".casefold():
            from . import oma_setting_string

            return oma_setting_string.OmaSettingString()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.omaSettingStringXml".casefold():
            from . import oma_setting_string_xml

            return oma_setting_string_xml.OmaSettingStringXml()
        return OmaSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import oma_setting_base64, oma_setting_boolean, oma_setting_date_time, oma_setting_floating_point, oma_setting_integer, oma_setting_string, oma_setting_string_xml

        from . import oma_setting_base64, oma_setting_boolean, oma_setting_date_time, oma_setting_floating_point, oma_setting_integer, oma_setting_string, oma_setting_string_xml

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "omaUri": lambda n : setattr(self, 'oma_uri', n.get_str_value()),
            "secretReferenceValueId": lambda n : setattr(self, 'secret_reference_value_id', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("omaUri", self.oma_uri)
        writer.write_additional_data_value(self.additional_data)
    

