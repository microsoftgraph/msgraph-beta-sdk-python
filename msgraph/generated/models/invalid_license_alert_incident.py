from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

class InvalidLicenseAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    def __init__(self,) -> None:
        """
        Instantiates a new InvalidLicenseAlertIncident and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.invalidLicenseAlertIncident"
        # The tenantLicenseStatus property
        self._tenant_license_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvalidLicenseAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InvalidLicenseAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InvalidLicenseAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantLicenseStatus": lambda n : setattr(self, 'tenant_license_status', n.get_str_value()),
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
        writer.write_str_value("tenantLicenseStatus", self.tenant_license_status)
    
    @property
    def tenant_license_status(self,) -> Optional[str]:
        """
        Gets the tenantLicenseStatus property value. The tenantLicenseStatus property
        Returns: Optional[str]
        """
        return self._tenant_license_status
    
    @tenant_license_status.setter
    def tenant_license_status(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantLicenseStatus property value. The tenantLicenseStatus property
        Args:
            value: Value to set for the tenant_license_status property.
        """
        self._tenant_license_status = value
    

