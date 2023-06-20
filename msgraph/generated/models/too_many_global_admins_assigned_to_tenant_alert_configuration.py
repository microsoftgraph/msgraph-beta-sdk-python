from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_configuration

from . import unified_role_management_alert_configuration

@dataclass
class TooManyGlobalAdminsAssignedToTenantAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    odata_type = "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration"
    # The globalAdminCountThreshold property
    global_admin_count_threshold: Optional[int] = None
    # The percentageOfGlobalAdminsOutOfRolesThreshold property
    percentage_of_global_admins_out_of_roles_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TooManyGlobalAdminsAssignedToTenantAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_configuration

        from . import unified_role_management_alert_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "globalAdminCountThreshold": lambda n : setattr(self, 'global_admin_count_threshold', n.get_int_value()),
            "percentageOfGlobalAdminsOutOfRolesThreshold": lambda n : setattr(self, 'percentage_of_global_admins_out_of_roles_threshold', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("globalAdminCountThreshold", self.global_admin_count_threshold)
        writer.write_int_value("percentageOfGlobalAdminsOutOfRolesThreshold", self.percentage_of_global_admins_out_of_roles_threshold)
    

