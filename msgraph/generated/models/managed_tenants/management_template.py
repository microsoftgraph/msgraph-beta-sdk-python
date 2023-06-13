from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_category, management_provider, management_template_collection, management_template_step, template_parameter, workload_action
    from .. import action_url, entity

from .. import entity

@dataclass
class ManagementTemplate(entity.Entity):
    # The management category for the management template. Possible values are: custom, devices, identity, unknownFutureValue. Required. Read-only.
    category: Optional[management_category.ManagementCategory] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime] = None
    # The description for the management template. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the management template. Required. Read-only.
    display_name: Optional[str] = None
    # The informationLinks property
    information_links: Optional[List[action_url.ActionUrl]] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime] = None
    # The managementTemplateCollections property
    management_template_collections: Optional[List[management_template_collection.ManagementTemplateCollection]] = None
    # The managementTemplateSteps property
    management_template_steps: Optional[List[management_template_step.ManagementTemplateStep]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of parameters used by the management template. Optional. Read-only.
    parameters: Optional[List[template_parameter.TemplateParameter]] = None
    # The priority property
    priority: Optional[int] = None
    # The provider property
    provider: Optional[management_provider.ManagementProvider] = None
    # The userImpact property
    user_impact: Optional[str] = None
    # The version property
    version: Optional[int] = None
    # The collection of workload actions associated with the management template. Optional. Read-only.
    workload_actions: Optional[List[workload_action.WorkloadAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_category, management_provider, management_template_collection, management_template_step, template_parameter, workload_action
        from .. import action_url, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationLinks": lambda n : setattr(self, 'information_links', n.get_collection_of_object_values(action_url.ActionUrl)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplateCollections": lambda n : setattr(self, 'management_template_collections', n.get_collection_of_object_values(management_template_collection.ManagementTemplateCollection)),
            "managementTemplateSteps": lambda n : setattr(self, 'management_template_steps', n.get_collection_of_object_values(management_template_step.ManagementTemplateStep)),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(template_parameter.TemplateParameter)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(management_provider.ManagementProvider)),
            "userImpact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "workloadActions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(workload_action.WorkloadAction)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("informationLinks", self.information_links)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_collection_of_object_values("managementTemplateCollections", self.management_template_collections)
        writer.write_collection_of_object_values("managementTemplateSteps", self.management_template_steps)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("userImpact", self.user_impact)
        writer.write_int_value("version", self.version)
        writer.write_collection_of_object_values("workloadActions", self.workload_actions)
    

