from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_peripheral_health = lazy_import('msgraph.generated.models.teamwork_peripheral_health')

class TeamworkHardwareHealth(AdditionalDataHolder, Parsable):
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
    def compute_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the computeHealth property value. The system health details for a teamworkDevice.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._compute_health
    
    @compute_health.setter
    def compute_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the computeHealth property value. The system health details for a teamworkDevice.
        Args:
            value: Value to set for the computeHealth property.
        """
        self._compute_health = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkHardwareHealth and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The system health details for a teamworkDevice.
        self._compute_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The health details about the HDMI ingest of a device.
        self._hdmi_ingest_health: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHardwareHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkHardwareHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compute_health": lambda n : setattr(self, 'compute_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "hdmi_ingest_health": lambda n : setattr(self, 'hdmi_ingest_health', n.get_object_value(teamwork_peripheral_health.TeamworkPeripheralHealth)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def hdmi_ingest_health(self,) -> Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]:
        """
        Gets the hdmiIngestHealth property value. The health details about the HDMI ingest of a device.
        Returns: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth]
        """
        return self._hdmi_ingest_health
    
    @hdmi_ingest_health.setter
    def hdmi_ingest_health(self,value: Optional[teamwork_peripheral_health.TeamworkPeripheralHealth] = None) -> None:
        """
        Sets the hdmiIngestHealth property value. The health details about the HDMI ingest of a device.
        Args:
            value: Value to set for the hdmiIngestHealth property.
        """
        self._hdmi_ingest_health = value
    
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
        writer.write_object_value("computeHealth", self.compute_health)
        writer.write_object_value("hdmiIngestHealth", self.hdmi_ingest_health)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

