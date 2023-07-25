from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.teams_app_permission_set import TeamsAppPermissionSet

@dataclass
class UpgradePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The consentedPermissionSet property
    consented_permission_set: Optional[TeamsAppPermissionSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpgradePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpgradePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpgradePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.teams_app_permission_set import TeamsAppPermissionSet

        from ......models.teams_app_permission_set import TeamsAppPermissionSet

        fields: Dict[str, Callable[[Any], None]] = {
            "consentedPermissionSet": lambda n : setattr(self, 'consented_permission_set', n.get_object_value(TeamsAppPermissionSet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("consentedPermissionSet", self.consented_permission_set)
        writer.write_additional_data_value(self.additional_data)
    

