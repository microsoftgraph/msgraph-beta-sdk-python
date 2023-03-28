from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_content_camera_configuration, teamwork_peripheral

class TeamworkCameraConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkCameraConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cameras property
        self._cameras: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None
        # The configuration for the content camera.
        self._content_camera_configuration: Optional[teamwork_content_camera_configuration.TeamworkContentCameraConfiguration] = None
        # The defaultContentCamera property
        self._default_content_camera: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def cameras(self,) -> Optional[List[teamwork_peripheral.TeamworkPeripheral]]:
        """
        Gets the cameras property value. The cameras property
        Returns: Optional[List[teamwork_peripheral.TeamworkPeripheral]]
        """
        return self._cameras
    
    @cameras.setter
    def cameras(self,value: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None) -> None:
        """
        Sets the cameras property value. The cameras property
        Args:
            value: Value to set for the cameras property.
        """
        self._cameras = value
    
    @property
    def content_camera_configuration(self,) -> Optional[teamwork_content_camera_configuration.TeamworkContentCameraConfiguration]:
        """
        Gets the contentCameraConfiguration property value. The configuration for the content camera.
        Returns: Optional[teamwork_content_camera_configuration.TeamworkContentCameraConfiguration]
        """
        return self._content_camera_configuration
    
    @content_camera_configuration.setter
    def content_camera_configuration(self,value: Optional[teamwork_content_camera_configuration.TeamworkContentCameraConfiguration] = None) -> None:
        """
        Sets the contentCameraConfiguration property value. The configuration for the content camera.
        Args:
            value: Value to set for the content_camera_configuration property.
        """
        self._content_camera_configuration = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkCameraConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkCameraConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkCameraConfiguration()
    
    @property
    def default_content_camera(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the defaultContentCamera property value. The defaultContentCamera property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._default_content_camera
    
    @default_content_camera.setter
    def default_content_camera(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the defaultContentCamera property value. The defaultContentCamera property
        Args:
            value: Value to set for the default_content_camera property.
        """
        self._default_content_camera = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_content_camera_configuration, teamwork_peripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "cameras": lambda n : setattr(self, 'cameras', n.get_collection_of_object_values(teamwork_peripheral.TeamworkPeripheral)),
            "contentCameraConfiguration": lambda n : setattr(self, 'content_camera_configuration', n.get_object_value(teamwork_content_camera_configuration.TeamworkContentCameraConfiguration)),
            "defaultContentCamera": lambda n : setattr(self, 'default_content_camera', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("cameras", self.cameras)
        writer.write_object_value("contentCameraConfiguration", self.content_camera_configuration)
        writer.write_object_value("defaultContentCamera", self.default_content_camera)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

