from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_capability, cloud_pc_remote_action_name

@dataclass
class CloudPcRemoteActionCapability(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates the state of the supported action capability to perform a Cloud PC remote action. Possible values are: enabled, disabled. Default value is enabled.
    action_capability: Optional[action_capability.ActionCapability] = None
    # The name of the supported Cloud PC remote action. Possible values are: unknown, restart, rename, restore, resize, reprovision, troubleShoot, changeUserAccountType, placeUnderReview. Default value is unknown.
    action_name: Optional[cloud_pc_remote_action_name.CloudPcRemoteActionName] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRemoteActionCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRemoteActionCapability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcRemoteActionCapability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_capability, cloud_pc_remote_action_name

        fields: Dict[str, Callable[[Any], None]] = {
            "actionCapability": lambda n : setattr(self, 'action_capability', n.get_enum_value(action_capability.ActionCapability)),
            "actionName": lambda n : setattr(self, 'action_name', n.get_enum_value(cloud_pc_remote_action_name.CloudPcRemoteActionName)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("actionCapability", self.action_capability)
        writer.write_enum_value("actionName", self.action_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

