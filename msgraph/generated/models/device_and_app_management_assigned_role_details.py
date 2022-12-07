from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceAndAppManagementAssignedRoleDetails(AdditionalDataHolder, Parsable):
    """
    The set of Role Definitions and Role Assignments assigned to a user.
    """
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
        Instantiates a new deviceAndAppManagementAssignedRoleDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Role Assignment IDs for the specifc Role Assignments assigned to a user. This property is read-only.
        self._role_assignment_ids: Optional[List[str]] = None
        # Role Definition IDs for the specifc Role Definitions assigned to a user. This property is read-only.
        self._role_definition_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignedRoleDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignedRoleDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAndAppManagementAssignedRoleDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role_assignment_ids": lambda n : setattr(self, 'role_assignment_ids', n.get_collection_of_primitive_values(str)),
            "role_definition_ids": lambda n : setattr(self, 'role_definition_ids', n.get_collection_of_primitive_values(str)),
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
    
    @property
    def role_assignment_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleAssignmentIds property value. Role Assignment IDs for the specifc Role Assignments assigned to a user. This property is read-only.
        Returns: Optional[List[str]]
        """
        return self._role_assignment_ids
    
    @role_assignment_ids.setter
    def role_assignment_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleAssignmentIds property value. Role Assignment IDs for the specifc Role Assignments assigned to a user. This property is read-only.
        Args:
            value: Value to set for the roleAssignmentIds property.
        """
        self._role_assignment_ids = value
    
    @property
    def role_definition_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleDefinitionIds property value. Role Definition IDs for the specifc Role Definitions assigned to a user. This property is read-only.
        Returns: Optional[List[str]]
        """
        return self._role_definition_ids
    
    @role_definition_ids.setter
    def role_definition_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleDefinitionIds property value. Role Definition IDs for the specifc Role Definitions assigned to a user. This property is read-only.
        Args:
            value: Value to set for the roleDefinitionIds property.
        """
        self._role_definition_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

