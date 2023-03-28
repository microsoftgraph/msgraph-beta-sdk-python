from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_peripheral

class TeamworkHardwareConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkHardwareConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The compute property
        self._compute: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The hdmiIngest property
        self._hdmi_ingest: Optional[teamwork_peripheral.TeamworkPeripheral] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The CPU model on the device.
        self._processor_model: Optional[str] = None
    
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
    def compute(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the compute property value. The compute property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._compute
    
    @compute.setter
    def compute(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the compute property value. The compute property
        Args:
            value: Value to set for the compute property.
        """
        self._compute = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHardwareConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkHardwareConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_peripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "compute": lambda n : setattr(self, 'compute', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "hdmiIngest": lambda n : setattr(self, 'hdmi_ingest', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processorModel": lambda n : setattr(self, 'processor_model', n.get_str_value()),
        }
        return fields
    
    @property
    def hdmi_ingest(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the hdmiIngest property value. The hdmiIngest property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._hdmi_ingest
    
    @hdmi_ingest.setter
    def hdmi_ingest(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the hdmiIngest property value. The hdmiIngest property
        Args:
            value: Value to set for the hdmi_ingest property.
        """
        self._hdmi_ingest = value
    
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
    def processor_model(self,) -> Optional[str]:
        """
        Gets the processorModel property value. The CPU model on the device.
        Returns: Optional[str]
        """
        return self._processor_model
    
    @processor_model.setter
    def processor_model(self,value: Optional[str] = None) -> None:
        """
        Sets the processorModel property value. The CPU model on the device.
        Args:
            value: Value to set for the processor_model property.
        """
        self._processor_model = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("compute", self.compute)
        writer.write_object_value("hdmiIngest", self.hdmi_ingest)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("processorModel", self.processor_model)
        writer.write_additional_data_value(self.additional_data)
    

