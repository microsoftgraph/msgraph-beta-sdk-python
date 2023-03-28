from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class DeviceManagementUserRightsLocalUserOrGroup(AdditionalDataHolder, Parsable):
    """
    Represents information for a local user or group used for user rights setting.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementUserRightsLocalUserOrGroup and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Admin’s description of this local user or group.
        self._description: Optional[str] = None
        # The name of this local user or group.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The security identifier of this local user or group (e.g. S-1-5-32-544).
        self._security_identifier: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementUserRightsLocalUserOrGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementUserRightsLocalUserOrGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementUserRightsLocalUserOrGroup()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin’s description of this local user or group.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin’s description of this local user or group.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of this local user or group.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of this local user or group.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    
    @property
    def security_identifier(self,) -> Optional[str]:
        """
        Gets the securityIdentifier property value. The security identifier of this local user or group (e.g. S-1-5-32-544).
        Returns: Optional[str]
        """
        return self._security_identifier
    
    @security_identifier.setter
    def security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the securityIdentifier property value. The security identifier of this local user or group (e.g. S-1-5-32-544).
        Args:
            value: Value to set for the security_identifier property.
        """
        self._security_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_additional_data_value(self.additional_data)
    

