from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_configuration

from . import unified_role_management_alert_configuration

class TooManyGlobalAdminsAssignedToTenantAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new TooManyGlobalAdminsAssignedToTenantAlertConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.tooManyGlobalAdminsAssignedToTenantAlertConfiguration"
        # The globalAdminCountThreshold property
        self._global_admin_count_threshold: Optional[int] = None
        # The percentageOfGlobalAdminsOutOfRolesThreshold property
        self._percentage_of_global_admins_out_of_roles_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TooManyGlobalAdminsAssignedToTenantAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TooManyGlobalAdminsAssignedToTenantAlertConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TooManyGlobalAdminsAssignedToTenantAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "globalAdminCountThreshold": lambda n : setattr(self, 'global_admin_count_threshold', n.get_int_value()),
            "percentageOfGlobalAdminsOutOfRolesThreshold": lambda n : setattr(self, 'percentage_of_global_admins_out_of_roles_threshold', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def global_admin_count_threshold(self,) -> Optional[int]:
        """
        Gets the globalAdminCountThreshold property value. The globalAdminCountThreshold property
        Returns: Optional[int]
        """
        return self._global_admin_count_threshold
    
    @global_admin_count_threshold.setter
    def global_admin_count_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the globalAdminCountThreshold property value. The globalAdminCountThreshold property
        Args:
            value: Value to set for the global_admin_count_threshold property.
        """
        self._global_admin_count_threshold = value
    
    @property
    def percentage_of_global_admins_out_of_roles_threshold(self,) -> Optional[int]:
        """
        Gets the percentageOfGlobalAdminsOutOfRolesThreshold property value. The percentageOfGlobalAdminsOutOfRolesThreshold property
        Returns: Optional[int]
        """
        return self._percentage_of_global_admins_out_of_roles_threshold
    
    @percentage_of_global_admins_out_of_roles_threshold.setter
    def percentage_of_global_admins_out_of_roles_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the percentageOfGlobalAdminsOutOfRolesThreshold property value. The percentageOfGlobalAdminsOutOfRolesThreshold property
        Args:
            value: Value to set for the percentage_of_global_admins_out_of_roles_threshold property.
        """
        self._percentage_of_global_admins_out_of_roles_threshold = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("globalAdminCountThreshold", self.global_admin_count_threshold)
        writer.write_int_value("percentageOfGlobalAdminsOutOfRolesThreshold", self.percentage_of_global_admins_out_of_roles_threshold)
    

