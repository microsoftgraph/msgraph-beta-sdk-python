from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..directory_object import DirectoryObject
    from ..entity import Entity
    from ..subject_set import SubjectSet
    from .agent_identity_lifecycle_policy import AgentIdentityLifecyclePolicy
    from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction
    from .lifecycle_policy_notification_settings import LifecyclePolicyNotificationSettings
    from .lifecycle_policy_rule import LifecyclePolicyRule
    from .lifecycle_policy_source import LifecyclePolicySource

from ..entity import Entity

@dataclass
class LifecyclePolicy(Entity, Parsable):
    # The createdBy property
    created_by: Optional[DirectoryObject] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The enforcementAction property
    enforcement_action: Optional[LifecyclePolicyEnforcementAction] = None
    # The gracePeriodInDays property
    grace_period_in_days: Optional[int] = None
    # The isEnabled property
    is_enabled: Optional[bool] = None
    # The lastModifiedBy property
    last_modified_by: Optional[DirectoryObject] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The notificationSchedule property
    notification_schedule: Optional[LifecyclePolicyNotificationSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policySource property
    policy_source: Optional[LifecyclePolicySource] = None
    # The rules property
    rules: Optional[list[LifecyclePolicyRule]] = None
    # The scope property
    scope: Optional[SubjectSet] = None
    # The versionNumber property
    version_number: Optional[int] = None
    # The versions property
    versions: Optional[list[LifecyclePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.agentIdentityLifecyclePolicy".casefold():
            from .agent_identity_lifecycle_policy import AgentIdentityLifecyclePolicy

            return AgentIdentityLifecyclePolicy()
        return LifecyclePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from ..subject_set import SubjectSet
        from .agent_identity_lifecycle_policy import AgentIdentityLifecyclePolicy
        from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction
        from .lifecycle_policy_notification_settings import LifecyclePolicyNotificationSettings
        from .lifecycle_policy_rule import LifecyclePolicyRule
        from .lifecycle_policy_source import LifecyclePolicySource

        from ..directory_object import DirectoryObject
        from ..entity import Entity
        from ..subject_set import SubjectSet
        from .agent_identity_lifecycle_policy import AgentIdentityLifecyclePolicy
        from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction
        from .lifecycle_policy_notification_settings import LifecyclePolicyNotificationSettings
        from .lifecycle_policy_rule import LifecyclePolicyRule
        from .lifecycle_policy_source import LifecyclePolicySource

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(DirectoryObject)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforcementAction": lambda n : setattr(self, 'enforcement_action', n.get_object_value(LifecyclePolicyEnforcementAction)),
            "gracePeriodInDays": lambda n : setattr(self, 'grace_period_in_days', n.get_int_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(DirectoryObject)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notificationSchedule": lambda n : setattr(self, 'notification_schedule', n.get_object_value(LifecyclePolicyNotificationSettings)),
            "policySource": lambda n : setattr(self, 'policy_source', n.get_enum_value(LifecyclePolicySource)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(LifecyclePolicyRule)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(SubjectSet)),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(LifecyclePolicy)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("enforcementAction", self.enforcement_action)
        writer.write_int_value("gracePeriodInDays", self.grace_period_in_days)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("notificationSchedule", self.notification_schedule)
        writer.write_enum_value("policySource", self.policy_source)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_object_value("scope", self.scope)
        writer.write_int_value("versionNumber", self.version_number)
        writer.write_collection_of_object_values("versions", self.versions)
    

