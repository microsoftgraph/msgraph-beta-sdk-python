from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance_decision_item_target

from . import access_review_instance_decision_item_target

@dataclass
class AccessReviewInstanceDecisionItemServicePrincipalTarget(access_review_instance_decision_item_target.AccessReviewInstanceDecisionItemTarget):
    odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalTarget"
    # The appId for the service principal entity being reviewed.
    app_id: Optional[str] = None
    # The display name of the service principal whose access is being reviewed.
    service_principal_display_name: Optional[str] = None
    # The servicePrincipalId property
    service_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemServicePrincipalTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemServicePrincipalTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItemServicePrincipalTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance_decision_item_target

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "servicePrincipalDisplayName": lambda n : setattr(self, 'service_principal_display_name', n.get_str_value()),
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("servicePrincipalDisplayName", self.service_principal_display_name)
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
    

