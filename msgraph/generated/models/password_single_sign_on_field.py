from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PasswordSingleSignOnField(AdditionalDataHolder, Parsable):
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
        Instantiates a new passwordSingleSignOnField and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Title/label override for customization.
        self._customized_label: Optional[str] = None
        # Label that would be used if no customizedLabel is provided. Read only.
        self._default_label: Optional[str] = None
        # Id used to identity the field type. This is an internal id and possible values are param_1, param_2, param_userName, param_password.
        self._field_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Type of the credential. The values can be text, password.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordSingleSignOnField:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordSingleSignOnField
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordSingleSignOnField()
    
    @property
    def customized_label(self,) -> Optional[str]:
        """
        Gets the customizedLabel property value. Title/label override for customization.
        Returns: Optional[str]
        """
        return self._customized_label
    
    @customized_label.setter
    def customized_label(self,value: Optional[str] = None) -> None:
        """
        Sets the customizedLabel property value. Title/label override for customization.
        Args:
            value: Value to set for the customizedLabel property.
        """
        self._customized_label = value
    
    @property
    def default_label(self,) -> Optional[str]:
        """
        Gets the defaultLabel property value. Label that would be used if no customizedLabel is provided. Read only.
        Returns: Optional[str]
        """
        return self._default_label
    
    @default_label.setter
    def default_label(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLabel property value. Label that would be used if no customizedLabel is provided. Read only.
        Args:
            value: Value to set for the defaultLabel property.
        """
        self._default_label = value
    
    @property
    def field_id(self,) -> Optional[str]:
        """
        Gets the fieldId property value. Id used to identity the field type. This is an internal id and possible values are param_1, param_2, param_userName, param_password.
        Returns: Optional[str]
        """
        return self._field_id
    
    @field_id.setter
    def field_id(self,value: Optional[str] = None) -> None:
        """
        Sets the fieldId property value. Id used to identity the field type. This is an internal id and possible values are param_1, param_2, param_userName, param_password.
        Args:
            value: Value to set for the fieldId property.
        """
        self._field_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "customized_label": lambda n : setattr(self, 'customized_label', n.get_str_value()),
            "default_label": lambda n : setattr(self, 'default_label', n.get_str_value()),
            "field_id": lambda n : setattr(self, 'field_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("customizedLabel", self.customized_label)
        writer.write_str_value("defaultLabel", self.default_label)
        writer.write_str_value("fieldId", self.field_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Type of the credential. The values can be text, password.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Type of the credential. The values can be text, password.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

