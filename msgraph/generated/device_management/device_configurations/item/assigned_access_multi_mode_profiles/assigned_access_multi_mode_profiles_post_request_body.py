from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.windows_assigned_access_profile import WindowsAssignedAccessProfile

@dataclass
class AssignedAccessMultiModeProfilesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The assignedAccessMultiModeProfiles property
    assigned_access_multi_mode_profiles: Optional[List[WindowsAssignedAccessProfile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedAccessMultiModeProfilesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignedAccessMultiModeProfilesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignedAccessMultiModeProfilesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.windows_assigned_access_profile import WindowsAssignedAccessProfile

        from .....models.windows_assigned_access_profile import WindowsAssignedAccessProfile

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedAccessMultiModeProfiles": lambda n : setattr(self, 'assigned_access_multi_mode_profiles', n.get_collection_of_object_values(WindowsAssignedAccessProfile)),
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
        writer.write_collection_of_object_values("assignedAccessMultiModeProfiles", self.assigned_access_multi_mode_profiles)
        writer.write_additional_data_value(self.additional_data)
    

