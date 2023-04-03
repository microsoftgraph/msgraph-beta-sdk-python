from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teams_app_resource_specific_permission

class TeamsAppPermissionSet(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppPermissionSet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The resourceSpecificPermissions property
        self._resource_specific_permissions: Optional[List[teams_app_resource_specific_permission.TeamsAppResourceSpecificPermission]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppPermissionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppPermissionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppPermissionSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teams_app_resource_specific_permission

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceSpecificPermissions": lambda n : setattr(self, 'resource_specific_permissions', n.get_collection_of_object_values(teams_app_resource_specific_permission.TeamsAppResourceSpecificPermission)),
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
    
    @property
    def resource_specific_permissions(self,) -> Optional[List[teams_app_resource_specific_permission.TeamsAppResourceSpecificPermission]]:
        """
        Gets the resourceSpecificPermissions property value. The resourceSpecificPermissions property
        Returns: Optional[List[teams_app_resource_specific_permission.TeamsAppResourceSpecificPermission]]
        """
        return self._resource_specific_permissions
    
    @resource_specific_permissions.setter
    def resource_specific_permissions(self,value: Optional[List[teams_app_resource_specific_permission.TeamsAppResourceSpecificPermission]] = None) -> None:
        """
        Sets the resourceSpecificPermissions property value. The resourceSpecificPermissions property
        Args:
            value: Value to set for the resource_specific_permissions property.
        """
        self._resource_specific_permissions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("resourceSpecificPermissions", self.resource_specific_permissions)
        writer.write_additional_data_value(self.additional_data)
    
