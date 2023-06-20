from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_content_camera_configuration, teamwork_peripheral

@dataclass
class TeamworkCameraConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The cameras property
    cameras: Optional[List[teamwork_peripheral.TeamworkPeripheral]] = None
    # The configuration for the content camera.
    content_camera_configuration: Optional[teamwork_content_camera_configuration.TeamworkContentCameraConfiguration] = None
    # The defaultContentCamera property
    default_content_camera: Optional[teamwork_peripheral.TeamworkPeripheral] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkCameraConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkCameraConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkCameraConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_content_camera_configuration, teamwork_peripheral

        from . import teamwork_content_camera_configuration, teamwork_peripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "cameras": lambda n : setattr(self, 'cameras', n.get_collection_of_object_values(teamwork_peripheral.TeamworkPeripheral)),
            "contentCameraConfiguration": lambda n : setattr(self, 'content_camera_configuration', n.get_object_value(teamwork_content_camera_configuration.TeamworkContentCameraConfiguration)),
            "defaultContentCamera": lambda n : setattr(self, 'default_content_camera', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("cameras", self.cameras)
        writer.write_object_value("contentCameraConfiguration", self.content_camera_configuration)
        writer.write_object_value("defaultContentCamera", self.default_content_camera)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

