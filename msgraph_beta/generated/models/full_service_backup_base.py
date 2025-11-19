from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .all_drives_backup import AllDrivesBackup
    from .all_mailboxes_backup import AllMailboxesBackup
    from .all_sites_backup import AllSitesBackup
    from .entity import Entity
    from .full_service_backup_disable_mode import FullServiceBackupDisableMode
    from .full_service_backup_status import FullServiceBackupStatus
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class FullServiceBackupBase(Entity, Parsable):
    # The actionOnExistingPolicy property
    action_on_existing_policy: Optional[FullServiceBackupDisableMode] = None
    # The lastModifiedBy property
    last_modified_by: Optional[IdentitySet] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The lastRunDateTime property
    last_run_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyId property
    policy_id: Optional[str] = None
    # The status property
    status: Optional[FullServiceBackupStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FullServiceBackupBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FullServiceBackupBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allDrivesBackup".casefold():
            from .all_drives_backup import AllDrivesBackup

            return AllDrivesBackup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allMailboxesBackup".casefold():
            from .all_mailboxes_backup import AllMailboxesBackup

            return AllMailboxesBackup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allSitesBackup".casefold():
            from .all_sites_backup import AllSitesBackup

            return AllSitesBackup()
        return FullServiceBackupBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .all_drives_backup import AllDrivesBackup
        from .all_mailboxes_backup import AllMailboxesBackup
        from .all_sites_backup import AllSitesBackup
        from .entity import Entity
        from .full_service_backup_disable_mode import FullServiceBackupDisableMode
        from .full_service_backup_status import FullServiceBackupStatus
        from .identity_set import IdentitySet

        from .all_drives_backup import AllDrivesBackup
        from .all_mailboxes_backup import AllMailboxesBackup
        from .all_sites_backup import AllSitesBackup
        from .entity import Entity
        from .full_service_backup_disable_mode import FullServiceBackupDisableMode
        from .full_service_backup_status import FullServiceBackupStatus
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "actionOnExistingPolicy": lambda n : setattr(self, 'action_on_existing_policy', n.get_enum_value(FullServiceBackupDisableMode)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FullServiceBackupStatus)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("actionOnExistingPolicy", self.action_on_existing_policy)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_enum_value("status", self.status)
    

