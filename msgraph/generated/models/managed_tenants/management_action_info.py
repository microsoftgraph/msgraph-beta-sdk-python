from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ManagementActionInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new managementActionInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier for the management action. Required. Read-only.
        self._management_action_id: Optional[str] = None
        # The identifier for the management template. Required. Read-only.
        self._management_template_id: Optional[str] = None
        # The managementTemplateVersion property
        self._management_template_version: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementActionInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementActionInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "managementActionId": lambda n : setattr(self, 'management_action_id', n.get_str_value()),
            "managementTemplateId": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "managementTemplateVersion": lambda n : setattr(self, 'management_template_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def management_action_id(self,) -> Optional[str]:
        """
        Gets the managementActionId property value. The identifier for the management action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_action_id
    
    @management_action_id.setter
    def management_action_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementActionId property value. The identifier for the management action. Required. Read-only.
        Args:
            value: Value to set for the management_action_id property.
        """
        self._management_action_id = value
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The identifier for the management template. Required. Read-only.
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The identifier for the management template. Required. Read-only.
        Args:
            value: Value to set for the management_template_id property.
        """
        self._management_template_id = value
    
    @property
    def management_template_version(self,) -> Optional[int]:
        """
        Gets the managementTemplateVersion property value. The managementTemplateVersion property
        Returns: Optional[int]
        """
        return self._management_template_version
    
    @management_template_version.setter
    def management_template_version(self,value: Optional[int] = None) -> None:
        """
        Sets the managementTemplateVersion property value. The managementTemplateVersion property
        Args:
            value: Value to set for the management_template_version property.
        """
        self._management_template_version = value
    
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
        writer.write_str_value("managementActionId", self.management_action_id)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_int_value("managementTemplateVersion", self.management_template_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

