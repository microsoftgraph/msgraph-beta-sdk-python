from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import entity

from .. import entity

class ConditionalAccessPolicyCoverage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessPolicyCoverage and sets the default values.
        """
        super().__init__()
        # The state for the conditional access policy. Possible values are: enabled, disabled, enabledForReportingButNotEnforced. Required. Read-only.
        self._conditional_access_policy_state: Optional[str] = None
        # The date and time the conditional access policy was last modified. Required. Read-only.
        self._latest_policy_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A flag indicating whether the conditional access policy requires device compliance. Required. Read-only.
        self._requires_device_compliance: Optional[bool] = None
        # The display name for the managed tenant. Required. Read-only.
        self._tenant_display_name: Optional[str] = None
    
    @property
    def conditional_access_policy_state(self,) -> Optional[str]:
        """
        Gets the conditionalAccessPolicyState property value. The state for the conditional access policy. Possible values are: enabled, disabled, enabledForReportingButNotEnforced. Required. Read-only.
        Returns: Optional[str]
        """
        return self._conditional_access_policy_state
    
    @conditional_access_policy_state.setter
    def conditional_access_policy_state(self,value: Optional[str] = None) -> None:
        """
        Sets the conditionalAccessPolicyState property value. The state for the conditional access policy. Possible values are: enabled, disabled, enabledForReportingButNotEnforced. Required. Read-only.
        Args:
            value: Value to set for the conditional_access_policy_state property.
        """
        self._conditional_access_policy_state = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPolicyCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicyCoverage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessPolicyCoverage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "conditionalAccessPolicyState": lambda n : setattr(self, 'conditional_access_policy_state', n.get_str_value()),
            "latestPolicyModifiedDateTime": lambda n : setattr(self, 'latest_policy_modified_date_time', n.get_datetime_value()),
            "requiresDeviceCompliance": lambda n : setattr(self, 'requires_device_compliance', n.get_bool_value()),
            "tenantDisplayName": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def latest_policy_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the latestPolicyModifiedDateTime property value. The date and time the conditional access policy was last modified. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._latest_policy_modified_date_time
    
    @latest_policy_modified_date_time.setter
    def latest_policy_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the latestPolicyModifiedDateTime property value. The date and time the conditional access policy was last modified. Required. Read-only.
        Args:
            value: Value to set for the latest_policy_modified_date_time property.
        """
        self._latest_policy_modified_date_time = value
    
    @property
    def requires_device_compliance(self,) -> Optional[bool]:
        """
        Gets the requiresDeviceCompliance property value. A flag indicating whether the conditional access policy requires device compliance. Required. Read-only.
        Returns: Optional[bool]
        """
        return self._requires_device_compliance
    
    @requires_device_compliance.setter
    def requires_device_compliance(self,value: Optional[bool] = None) -> None:
        """
        Sets the requiresDeviceCompliance property value. A flag indicating whether the conditional access policy requires device compliance. Required. Read-only.
        Args:
            value: Value to set for the requires_device_compliance property.
        """
        self._requires_device_compliance = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("conditionalAccessPolicyState", self.conditional_access_policy_state)
        writer.write_datetime_value("latestPolicyModifiedDateTime", self.latest_policy_modified_date_time)
        writer.write_bool_value("requiresDeviceCompliance", self.requires_device_compliance)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenant_display_name property.
        """
        self._tenant_display_name = value
    

