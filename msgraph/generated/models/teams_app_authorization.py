from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teams_app_permission_set

class TeamsAppAuthorization(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppAuthorization and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Set of permissions required by the teamsApp.
        self._required_permission_set: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppAuthorization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppAuthorization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppAuthorization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teams_app_permission_set

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requiredPermissionSet": lambda n : setattr(self, 'required_permission_set', n.get_object_value(teams_app_permission_set.TeamsAppPermissionSet)),
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
    def required_permission_set(self,) -> Optional[teams_app_permission_set.TeamsAppPermissionSet]:
        """
        Gets the requiredPermissionSet property value. Set of permissions required by the teamsApp.
        Returns: Optional[teams_app_permission_set.TeamsAppPermissionSet]
        """
        return self._required_permission_set
    
    @required_permission_set.setter
    def required_permission_set(self,value: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None) -> None:
        """
        Sets the requiredPermissionSet property value. Set of permissions required by the teamsApp.
        Args:
            value: Value to set for the required_permission_set property.
        """
        self._required_permission_set = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("requiredPermissionSet", self.required_permission_set)
        writer.write_additional_data_value(self.additional_data)
    

