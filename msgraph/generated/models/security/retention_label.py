from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_after_retention_period, behavior_during_retention_period, default_record_behavior, disposition_review_stage, retention_duration, retention_event_type, retention_trigger
    from .. import entity, identity_set

from .. import entity

@dataclass
class RetentionLabel(entity.Entity):
    # Specifies the action to take on a document with this label applied during the retention period. The possible values are: none, delete, startDispositionReview, unknownFutureValue.
    action_after_retention_period: Optional[action_after_retention_period.ActionAfterRetentionPeriod] = None
    # Specifies how the behavior of a document with this label should be during the retention period. The possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue.
    behavior_during_retention_period: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod] = None
    # Represents the user who created the retentionLabel.
    created_by: Optional[identity_set.IdentitySet] = None
    # Represents the date and time in which the retentionLabel is created.
    created_date_time: Optional[datetime] = None
    # Specifies the locked or unlocked state of a record label when it is created.The possible values are: startLocked, startUnlocked, unknownFutureValue.
    default_record_behavior: Optional[default_record_behavior.DefaultRecordBehavior] = None
    # Provides label information for the admin. Optional.
    description_for_admins: Optional[str] = None
    # Provides the label information for the user. Optional.
    description_for_users: Optional[str] = None
    # Unique string that defines a label name.
    display_name: Optional[str] = None
    # Review stages during which reviewers are notified to determine whether a document must be deleted or retained.
    disposition_review_stages: Optional[List[disposition_review_stage.DispositionReviewStage]] = None
    # Specifies whether the label is currently being used.
    is_in_use: Optional[bool] = None
    # Specifies the replacement label to be applied automatically after the retention period of the current label ends.
    label_to_be_applied: Optional[str] = None
    # The user who last modified the retentionLabel.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The latest date time when the retentionLabel was modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the number of days to retain the content.
    retention_duration: Optional[retention_duration.RetentionDuration] = None
    # The retentionEventType property
    retention_event_type: Optional[retention_event_type.RetentionEventType] = None
    # Specifies whether the retention duration is calculated from the content creation date, labeled date, or last modification date. The possible values are: dateLabeled, dateCreated, dateModified, dateOfEvent, unknownFutureValue.
    retention_trigger: Optional[retention_trigger.RetentionTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_after_retention_period, behavior_during_retention_period, default_record_behavior, disposition_review_stage, retention_duration, retention_event_type, retention_trigger
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "actionAfterRetentionPeriod": lambda n : setattr(self, 'action_after_retention_period', n.get_enum_value(action_after_retention_period.ActionAfterRetentionPeriod)),
            "behaviorDuringRetentionPeriod": lambda n : setattr(self, 'behavior_during_retention_period', n.get_enum_value(behavior_during_retention_period.BehaviorDuringRetentionPeriod)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultRecordBehavior": lambda n : setattr(self, 'default_record_behavior', n.get_enum_value(default_record_behavior.DefaultRecordBehavior)),
            "descriptionForAdmins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "descriptionForUsers": lambda n : setattr(self, 'description_for_users', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dispositionReviewStages": lambda n : setattr(self, 'disposition_review_stages', n.get_collection_of_object_values(disposition_review_stage.DispositionReviewStage)),
            "isInUse": lambda n : setattr(self, 'is_in_use', n.get_bool_value()),
            "labelToBeApplied": lambda n : setattr(self, 'label_to_be_applied', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "retentionDuration": lambda n : setattr(self, 'retention_duration', n.get_object_value(retention_duration.RetentionDuration)),
            "retentionEventType": lambda n : setattr(self, 'retention_event_type', n.get_object_value(retention_event_type.RetentionEventType)),
            "retentionTrigger": lambda n : setattr(self, 'retention_trigger', n.get_enum_value(retention_trigger.RetentionTrigger)),
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
        writer.write_enum_value("actionAfterRetentionPeriod", self.action_after_retention_period)
        writer.write_enum_value("behaviorDuringRetentionPeriod", self.behavior_during_retention_period)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultRecordBehavior", self.default_record_behavior)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForUsers", self.description_for_users)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("dispositionReviewStages", self.disposition_review_stages)
        writer.write_bool_value("isInUse", self.is_in_use)
        writer.write_str_value("labelToBeApplied", self.label_to_be_applied)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("retentionDuration", self.retention_duration)
        writer.write_object_value("retentionEventType", self.retention_event_type)
        writer.write_enum_value("retentionTrigger", self.retention_trigger)
    

