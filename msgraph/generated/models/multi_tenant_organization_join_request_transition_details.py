from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

@dataclass
class MultiTenantOrganizationJoinRequestTransitionDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The desiredMemberState property
    desired_member_state: Optional[MultiTenantOrganizationMemberState] = None
    # The details property
    details: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[MultiTenantOrganizationMemberProcessingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MultiTenantOrganizationJoinRequestTransitionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationJoinRequestTransitionDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationJoinRequestTransitionDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        fields: Dict[str, Callable[[Any], None]] = {
            "desiredMemberState": lambda n : setattr(self, 'desired_member_state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MultiTenantOrganizationMemberProcessingStatus)),
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
        writer.write_enum_value("desiredMemberState", self.desired_member_state)
        writer.write_str_value("details", self.details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

