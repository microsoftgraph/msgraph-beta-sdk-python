from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkMicrophoneConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The defaultMicrophone property
    default_microphone: Optional[TeamworkPeripheral] = None
    # True if the configured microphone is optional. False if the microphone is not optional and the health state of the device should be computed.
    is_microphone_optional: Optional[bool] = None
    # The microphones property
    microphones: Optional[List[TeamworkPeripheral]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkMicrophoneConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkMicrophoneConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkMicrophoneConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_peripheral import TeamworkPeripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultMicrophone": lambda n : setattr(self, 'default_microphone', n.get_object_value(TeamworkPeripheral)),
            "isMicrophoneOptional": lambda n : setattr(self, 'is_microphone_optional', n.get_bool_value()),
            "microphones": lambda n : setattr(self, 'microphones', n.get_collection_of_object_values(TeamworkPeripheral)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("defaultMicrophone", self.default_microphone)
        writer.write_bool_value("isMicrophoneOptional", self.is_microphone_optional)
        writer.write_collection_of_object_values("microphones", self.microphones)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

