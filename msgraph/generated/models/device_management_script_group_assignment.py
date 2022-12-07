from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementScriptGroupAssignment(entity.Entity):
    """
    Contains properties used to assign a device management script to a group.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementScriptGroupAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Id of the Azure Active Directory group we are targeting the script to.
        self._target_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementScriptGroupAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementScriptGroupAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementScriptGroupAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "target_group_id": lambda n : setattr(self, 'target_group_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("targetGroupId", self.target_group_id)
    
    @property
    def target_group_id(self,) -> Optional[str]:
        """
        Gets the targetGroupId property value. The Id of the Azure Active Directory group we are targeting the script to.
        Returns: Optional[str]
        """
        return self._target_group_id
    
    @target_group_id.setter
    def target_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetGroupId property value. The Id of the Azure Active Directory group we are targeting the script to.
        Args:
            value: Value to set for the targetGroupId property.
        """
        self._target_group_id = value
    

