from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teams_app_resource_specific_permission_type

class TeamsAppResourceSpecificPermission(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppResourceSpecificPermission and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The permissionType property
        self._permission_type: Optional[teams_app_resource_specific_permission_type.TeamsAppResourceSpecificPermissionType] = None
        # The permissionValue property
        self._permission_value: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppResourceSpecificPermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppResourceSpecificPermission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppResourceSpecificPermission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teams_app_resource_specific_permission_type

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_enum_value(teams_app_resource_specific_permission_type.TeamsAppResourceSpecificPermissionType)),
            "permissionValue": lambda n : setattr(self, 'permission_value', n.get_str_value()),
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
    def permission_type(self,) -> Optional[teams_app_resource_specific_permission_type.TeamsAppResourceSpecificPermissionType]:
        """
        Gets the permissionType property value. The permissionType property
        Returns: Optional[teams_app_resource_specific_permission_type.TeamsAppResourceSpecificPermissionType]
        """
        return self._permission_type
    
    @permission_type.setter
    def permission_type(self,value: Optional[teams_app_resource_specific_permission_type.TeamsAppResourceSpecificPermissionType] = None) -> None:
        """
        Sets the permissionType property value. The permissionType property
        Args:
            value: Value to set for the permission_type property.
        """
        self._permission_type = value
    
    @property
    def permission_value(self,) -> Optional[str]:
        """
        Gets the permissionValue property value. The permissionValue property
        Returns: Optional[str]
        """
        return self._permission_value
    
    @permission_value.setter
    def permission_value(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionValue property value. The permissionValue property
        Args:
            value: Value to set for the permission_value property.
        """
        self._permission_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("permissionType", self.permission_type)
        writer.write_str_value("permissionValue", self.permission_value)
        writer.write_additional_data_value(self.additional_data)
    

