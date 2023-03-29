from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import teams_app_permission_set

class UpgradePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new upgradePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The consentedPermissionSet property
        self._consented_permission_set: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None
    
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
    
    @property
    def consented_permission_set(self,) -> Optional[teams_app_permission_set.TeamsAppPermissionSet]:
        """
        Gets the consentedPermissionSet property value. The consentedPermissionSet property
        Returns: Optional[teams_app_permission_set.TeamsAppPermissionSet]
        """
        return self._consented_permission_set
    
    @consented_permission_set.setter
    def consented_permission_set(self,value: Optional[teams_app_permission_set.TeamsAppPermissionSet] = None) -> None:
        """
        Sets the consentedPermissionSet property value. The consentedPermissionSet property
        Args:
            value: Value to set for the consented_permission_set property.
        """
        self._consented_permission_set = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpgradePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpgradePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpgradePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models import teams_app_permission_set

        fields: Dict[str, Callable[[Any], None]] = {
            "consentedPermissionSet": lambda n : setattr(self, 'consented_permission_set', n.get_object_value(teams_app_permission_set.TeamsAppPermissionSet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("consentedPermissionSet", self.consented_permission_set)
        writer.write_additional_data_value(self.additional_data)
    

