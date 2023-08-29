from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class ConditionalAccessPolicyCoverage(Entity):
    # The state for the conditional access policy. Possible values are: enabled, disabled, enabledForReportingButNotEnforced. Required. Read-only.
    conditional_access_policy_state: Optional[str] = None
    # The date and time the conditional access policy was last modified. Required. Read-only.
    latest_policy_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A flag indicating whether the conditional access policy requires device compliance. Required. Read-only.
    requires_device_compliance: Optional[bool] = None
    # The display name for the managed tenant. Required. Read-only.
    tenant_display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPolicyCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicyCoverage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessPolicyCoverage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "conditionalAccessPolicyState": lambda n : setattr(self, 'conditional_access_policy_state', n.get_str_value()),
            "latestPolicyModifiedDateTime": lambda n : setattr(self, 'latest_policy_modified_date_time', n.get_datetime_value()),
            "requiresDeviceCompliance": lambda n : setattr(self, 'requires_device_compliance', n.get_bool_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("conditionalAccessPolicyState", self.conditional_access_policy_state)
        writer.write_datetime_value("latestPolicyModifiedDateTime", self.latest_policy_modified_date_time)
        writer.write_bool_value("requiresDeviceCompliance", self.requires_device_compliance)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
    

