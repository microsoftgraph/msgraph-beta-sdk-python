from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_category, management_template, management_template_step_version
    from .. import action_url, entity

from .. import entity

@dataclass
class ManagementTemplateStep(entity.Entity):
    # The acceptedVersion property
    accepted_version: Optional[management_template_step_version.ManagementTemplateStepVersion] = None
    # The category property
    category: Optional[management_category.ManagementCategory] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime] = None
    # The managementTemplate property
    management_template: Optional[management_template.ManagementTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The portalLink property
    portal_link: Optional[action_url.ActionUrl] = None
    # The priority property
    priority: Optional[int] = None
    # The versions property
    versions: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStep
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplateStep()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_category, management_template, management_template_step_version
        from .. import action_url, entity

        from . import management_category, management_template, management_template_step_version
        from .. import action_url, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptedVersion": lambda n : setattr(self, 'accepted_version', n.get_object_value(management_template_step_version.ManagementTemplateStepVersion)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplate": lambda n : setattr(self, 'management_template', n.get_object_value(management_template.ManagementTemplate)),
            "portalLink": lambda n : setattr(self, 'portal_link', n.get_object_value(action_url.ActionUrl)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(management_template_step_version.ManagementTemplateStepVersion)),
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
        writer.write_object_value("acceptedVersion", self.accepted_version)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_object_value("managementTemplate", self.management_template)
        writer.write_object_value("portalLink", self.portal_link)
        writer.write_int_value("priority", self.priority)
        writer.write_collection_of_object_values("versions", self.versions)
    

