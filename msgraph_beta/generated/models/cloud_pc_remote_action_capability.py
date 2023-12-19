from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_remote_action_capability_action_capability import CloudPcRemoteActionCapability_actionCapability
    from .cloud_pc_remote_action_capability_action_name import CloudPcRemoteActionCapability_actionName

@dataclass
class CloudPcRemoteActionCapability(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates the state of the supported action capability to perform a Cloud PC remote action. Possible values are: enabled, disabled. Default value is enabled.
    action_capability: Optional[CloudPcRemoteActionCapability_actionCapability] = None
    # The name of the supported Cloud PC remote action. Possible values are: unknown, restart, rename, restore, resize, reprovision, troubleShoot, changeUserAccountType, placeUnderReview. Default value is unknown.
    action_name: Optional[CloudPcRemoteActionCapability_actionName] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRemoteActionCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRemoteActionCapability
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcRemoteActionCapability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_remote_action_capability_action_capability import CloudPcRemoteActionCapability_actionCapability
        from .cloud_pc_remote_action_capability_action_name import CloudPcRemoteActionCapability_actionName

        from .cloud_pc_remote_action_capability_action_capability import CloudPcRemoteActionCapability_actionCapability
        from .cloud_pc_remote_action_capability_action_name import CloudPcRemoteActionCapability_actionName

        fields: Dict[str, Callable[[Any], None]] = {
            "actionCapability": lambda n : setattr(self, 'action_capability', n.get_enum_value(CloudPcRemoteActionCapability_actionCapability)),
            "actionName": lambda n : setattr(self, 'action_name', n.get_enum_value(CloudPcRemoteActionCapability_actionName)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("actionCapability", self.action_capability)
        writer.write_enum_value("actionName", self.action_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

