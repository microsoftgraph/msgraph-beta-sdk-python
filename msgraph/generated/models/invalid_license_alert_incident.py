from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

@dataclass
class InvalidLicenseAlertIncident(UnifiedRoleManagementAlertIncident):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.invalidLicenseAlertIncident"
    # Status of the tenant's Microsoft Entra ID P2 license.
    tenant_license_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvalidLicenseAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvalidLicenseAlertIncident
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InvalidLicenseAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        from .unified_role_management_alert_incident import UnifiedRoleManagementAlertIncident

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantLicenseStatus": lambda n : setattr(self, 'tenant_license_status', n.get_str_value()),
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
        writer.write_str_value("tenantLicenseStatus", self.tenant_license_status)
    

