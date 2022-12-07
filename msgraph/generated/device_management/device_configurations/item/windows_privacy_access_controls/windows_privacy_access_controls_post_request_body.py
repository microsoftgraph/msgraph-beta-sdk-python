from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_privacy_data_access_control_item = lazy_import('msgraph.generated.models.windows_privacy_data_access_control_item')

class WindowsPrivacyAccessControlsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the windowsPrivacyAccessControls method.
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
        Instantiates a new windowsPrivacyAccessControlsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The windowsPrivacyAccessControls property
        self._windows_privacy_access_controls: Optional[List[windows_privacy_data_access_control_item.WindowsPrivacyDataAccessControlItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPrivacyAccessControlsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPrivacyAccessControlsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPrivacyAccessControlsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "windows_privacy_access_controls": lambda n : setattr(self, 'windows_privacy_access_controls', n.get_collection_of_object_values(windows_privacy_data_access_control_item.WindowsPrivacyDataAccessControlItem)),
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
        writer.write_collection_of_object_values("windowsPrivacyAccessControls", self.windows_privacy_access_controls)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def windows_privacy_access_controls(self,) -> Optional[List[windows_privacy_data_access_control_item.WindowsPrivacyDataAccessControlItem]]:
        """
        Gets the windowsPrivacyAccessControls property value. The windowsPrivacyAccessControls property
        Returns: Optional[List[windows_privacy_data_access_control_item.WindowsPrivacyDataAccessControlItem]]
        """
        return self._windows_privacy_access_controls
    
    @windows_privacy_access_controls.setter
    def windows_privacy_access_controls(self,value: Optional[List[windows_privacy_data_access_control_item.WindowsPrivacyDataAccessControlItem]] = None) -> None:
        """
        Sets the windowsPrivacyAccessControls property value. The windowsPrivacyAccessControls property
        Args:
            value: Value to set for the windowsPrivacyAccessControls property.
        """
        self._windows_privacy_access_controls = value
    

