from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

management_parameter_value_type = lazy_import('msgraph.generated.models.managed_tenants.management_parameter_value_type')

class Setting(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new setting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name for the setting. Required. Read-only.
        self._display_name: Optional[str] = None
        # The value for the setting serialized as string of JSON. Required. Read-only.
        self._json_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A flag indicating whether the setting can be override existing configurations when applied. Required. Read-only.
        self._overwrite_allowed: Optional[bool] = None
        # The settingId property
        self._setting_id: Optional[str] = None
        # The valueType property
        self._value_type: Optional[management_parameter_value_type.ManagementParameterValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Setting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Setting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Setting()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the setting. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the setting. Required. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "json_value": lambda n : setattr(self, 'json_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overwrite_allowed": lambda n : setattr(self, 'overwrite_allowed', n.get_bool_value()),
            "setting_id": lambda n : setattr(self, 'setting_id', n.get_str_value()),
            "value_type": lambda n : setattr(self, 'value_type', n.get_enum_value(management_parameter_value_type.ManagementParameterValueType)),
        }
        return fields
    
    @property
    def json_value(self,) -> Optional[str]:
        """
        Gets the jsonValue property value. The value for the setting serialized as string of JSON. Required. Read-only.
        Returns: Optional[str]
        """
        return self._json_value
    
    @json_value.setter
    def json_value(self,value: Optional[str] = None) -> None:
        """
        Sets the jsonValue property value. The value for the setting serialized as string of JSON. Required. Read-only.
        Args:
            value: Value to set for the jsonValue property.
        """
        self._json_value = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def overwrite_allowed(self,) -> Optional[bool]:
        """
        Gets the overwriteAllowed property value. A flag indicating whether the setting can be override existing configurations when applied. Required. Read-only.
        Returns: Optional[bool]
        """
        return self._overwrite_allowed
    
    @overwrite_allowed.setter
    def overwrite_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the overwriteAllowed property value. A flag indicating whether the setting can be override existing configurations when applied. Required. Read-only.
        Args:
            value: Value to set for the overwriteAllowed property.
        """
        self._overwrite_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("jsonValue", self.json_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("overwriteAllowed", self.overwrite_allowed)
        writer.write_str_value("settingId", self.setting_id)
        writer.write_enum_value("valueType", self.value_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def setting_id(self,) -> Optional[str]:
        """
        Gets the settingId property value. The settingId property
        Returns: Optional[str]
        """
        return self._setting_id
    
    @setting_id.setter
    def setting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingId property value. The settingId property
        Args:
            value: Value to set for the settingId property.
        """
        self._setting_id = value
    
    @property
    def value_type(self,) -> Optional[management_parameter_value_type.ManagementParameterValueType]:
        """
        Gets the valueType property value. The valueType property
        Returns: Optional[management_parameter_value_type.ManagementParameterValueType]
        """
        return self._value_type
    
    @value_type.setter
    def value_type(self,value: Optional[management_parameter_value_type.ManagementParameterValueType] = None) -> None:
        """
        Sets the valueType property value. The valueType property
        Args:
            value: Value to set for the valueType property.
        """
        self._value_type = value
    

