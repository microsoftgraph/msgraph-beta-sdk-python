from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import deployment_state_reason, deployment_state_value, requested_deployment_state_value

@dataclass
class DeploymentState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The effectiveValue property
    effective_value: Optional[deployment_state_value.DeploymentStateValue] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the reasons the deployment has its state value. Read-only.
    reasons: Optional[List[deployment_state_reason.DeploymentStateReason]] = None
    # The requestedValue property
    requested_value: Optional[requested_deployment_state_value.RequestedDeploymentStateValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeploymentState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeploymentState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import deployment_state_reason, deployment_state_value, requested_deployment_state_value

        from . import deployment_state_reason, deployment_state_value, requested_deployment_state_value

        fields: Dict[str, Callable[[Any], None]] = {
            "effectiveValue": lambda n : setattr(self, 'effective_value', n.get_enum_value(deployment_state_value.DeploymentStateValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reasons": lambda n : setattr(self, 'reasons', n.get_collection_of_object_values(deployment_state_reason.DeploymentStateReason)),
            "requestedValue": lambda n : setattr(self, 'requested_value', n.get_enum_value(requested_deployment_state_value.RequestedDeploymentStateValue)),
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
        writer.write_enum_value("effectiveValue", self.effective_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("reasons", self.reasons)
        writer.write_enum_value("requestedValue", self.requested_value)
        writer.write_additional_data_value(self.additional_data)
    

