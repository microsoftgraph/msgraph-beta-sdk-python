from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkContentCameraConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkContentCameraConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # True if the content camera is inverted.
        self._is_content_camera_inverted: Optional[bool] = None
        # True if the content camera is optional.
        self._is_content_camera_optional: Optional[bool] = None
        # True if the content enhancement is enabled.
        self._is_content_enhancement_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkContentCameraConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkContentCameraConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkContentCameraConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_content_camera_inverted": lambda n : setattr(self, 'is_content_camera_inverted', n.get_bool_value()),
            "is_content_camera_optional": lambda n : setattr(self, 'is_content_camera_optional', n.get_bool_value()),
            "is_content_enhancement_enabled": lambda n : setattr(self, 'is_content_enhancement_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_content_camera_inverted(self,) -> Optional[bool]:
        """
        Gets the isContentCameraInverted property value. True if the content camera is inverted.
        Returns: Optional[bool]
        """
        return self._is_content_camera_inverted
    
    @is_content_camera_inverted.setter
    def is_content_camera_inverted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentCameraInverted property value. True if the content camera is inverted.
        Args:
            value: Value to set for the isContentCameraInverted property.
        """
        self._is_content_camera_inverted = value
    
    @property
    def is_content_camera_optional(self,) -> Optional[bool]:
        """
        Gets the isContentCameraOptional property value. True if the content camera is optional.
        Returns: Optional[bool]
        """
        return self._is_content_camera_optional
    
    @is_content_camera_optional.setter
    def is_content_camera_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentCameraOptional property value. True if the content camera is optional.
        Args:
            value: Value to set for the isContentCameraOptional property.
        """
        self._is_content_camera_optional = value
    
    @property
    def is_content_enhancement_enabled(self,) -> Optional[bool]:
        """
        Gets the isContentEnhancementEnabled property value. True if the content enhancement is enabled.
        Returns: Optional[bool]
        """
        return self._is_content_enhancement_enabled
    
    @is_content_enhancement_enabled.setter
    def is_content_enhancement_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isContentEnhancementEnabled property value. True if the content enhancement is enabled.
        Args:
            value: Value to set for the isContentEnhancementEnabled property.
        """
        self._is_content_enhancement_enabled = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isContentCameraInverted", self.is_content_camera_inverted)
        writer.write_bool_value("isContentCameraOptional", self.is_content_camera_optional)
        writer.write_bool_value("isContentEnhancementEnabled", self.is_content_enhancement_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

