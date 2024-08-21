from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deployment_state_reason import DeploymentStateReason
    from .deployment_state_value import DeploymentStateValue
    from .requested_deployment_state_value import RequestedDeploymentStateValue

@dataclass
class DeploymentState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The effectiveValue property
    effective_value: Optional[DeploymentStateValue] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the reasons the deployment has its state value. Read-only.
    reasons: Optional[List[DeploymentStateReason]] = None
    # The requestedValue property
    requested_value: Optional[RequestedDeploymentStateValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeploymentState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeploymentState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .deployment_state_reason import DeploymentStateReason
        from .deployment_state_value import DeploymentStateValue
        from .requested_deployment_state_value import RequestedDeploymentStateValue

        from .deployment_state_reason import DeploymentStateReason
        from .deployment_state_value import DeploymentStateValue
        from .requested_deployment_state_value import RequestedDeploymentStateValue

        fields: Dict[str, Callable[[Any], None]] = {
            "effectiveValue": lambda n : setattr(self, 'effective_value', n.get_enum_value(DeploymentStateValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reasons": lambda n : setattr(self, 'reasons', n.get_collection_of_object_values(DeploymentStateReason)),
            "requestedValue": lambda n : setattr(self, 'requested_value', n.get_enum_value(RequestedDeploymentStateValue)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("effectiveValue", self.effective_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("reasons", self.reasons)
        writer.write_enum_value("requestedValue", self.requested_value)
        writer.write_additional_data_value(self.additional_data)
    

