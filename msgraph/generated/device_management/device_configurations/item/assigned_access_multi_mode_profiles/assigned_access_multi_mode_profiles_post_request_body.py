from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_assigned_access_profile = lazy_import('msgraph.generated.models.windows_assigned_access_profile')

class AssignedAccessMultiModeProfilesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assignedAccessMultiModeProfiles method.
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
    
    @property
    def assigned_access_multi_mode_profiles(self,) -> Optional[List[windows_assigned_access_profile.WindowsAssignedAccessProfile]]:
        """
        Gets the assignedAccessMultiModeProfiles property value. The assignedAccessMultiModeProfiles property
        Returns: Optional[List[windows_assigned_access_profile.WindowsAssignedAccessProfile]]
        """
        return self._assigned_access_multi_mode_profiles
    
    @assigned_access_multi_mode_profiles.setter
    def assigned_access_multi_mode_profiles(self,value: Optional[List[windows_assigned_access_profile.WindowsAssignedAccessProfile]] = None) -> None:
        """
        Sets the assignedAccessMultiModeProfiles property value. The assignedAccessMultiModeProfiles property
        Args:
            value: Value to set for the assignedAccessMultiModeProfiles property.
        """
        self._assigned_access_multi_mode_profiles = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignedAccessMultiModeProfilesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignedAccessMultiModeProfiles property
        self._assigned_access_multi_mode_profiles: Optional[List[windows_assigned_access_profile.WindowsAssignedAccessProfile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedAccessMultiModeProfilesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignedAccessMultiModeProfilesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignedAccessMultiModeProfilesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_access_multi_mode_profiles": lambda n : setattr(self, 'assigned_access_multi_mode_profiles', n.get_collection_of_object_values(windows_assigned_access_profile.WindowsAssignedAccessProfile)),
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
        writer.write_collection_of_object_values("assignedAccessMultiModeProfiles", self.assigned_access_multi_mode_profiles)
        writer.write_additional_data_value(self.additional_data)
    

