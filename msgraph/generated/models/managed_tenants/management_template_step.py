from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_url = lazy_import('msgraph.generated.models.action_url')
entity = lazy_import('msgraph.generated.models.entity')
management_category = lazy_import('msgraph.generated.models.managed_tenants.management_category')
management_template = lazy_import('msgraph.generated.models.managed_tenants.management_template')
management_template_step_version = lazy_import('msgraph.generated.models.managed_tenants.management_template_step_version')

class ManagementTemplateStep(entity.Entity):
    @property
    def accepted_version(self,) -> Optional[management_template_step_version.ManagementTemplateStepVersion]:
        """
        Gets the acceptedVersion property value. The acceptedVersion property
        Returns: Optional[management_template_step_version.ManagementTemplateStepVersion]
        """
        return self._accepted_version
    
    @accepted_version.setter
    def accepted_version(self,value: Optional[management_template_step_version.ManagementTemplateStepVersion] = None) -> None:
        """
        Sets the acceptedVersion property value. The acceptedVersion property
        Args:
            value: Value to set for the acceptedVersion property.
        """
        self._accepted_version = value
    
    @property
    def category(self,) -> Optional[management_category.ManagementCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[management_category.ManagementCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[management_category.ManagementCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateStep and sets the default values.
        """
        super().__init__()
        # The acceptedVersion property
        self._accepted_version: Optional[management_template_step_version.ManagementTemplateStepVersion] = None
        # The category property
        self._category: Optional[management_category.ManagementCategory] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The managementTemplate property
        self._management_template: Optional[management_template.ManagementTemplate] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The portalLink property
        self._portal_link: Optional[action_url.ActionUrl] = None
        # The priority property
        self._priority: Optional[int] = None
        # The versions property
        self._versions: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStep
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateStep()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accepted_version": lambda n : setattr(self, 'accepted_version', n.get_object_value(management_template_step_version.ManagementTemplateStepVersion)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "management_template": lambda n : setattr(self, 'management_template', n.get_object_value(management_template.ManagementTemplate)),
            "portal_link": lambda n : setattr(self, 'portal_link', n.get_object_value(action_url.ActionUrl)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(management_template_step_version.ManagementTemplateStepVersion)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def management_template(self,) -> Optional[management_template.ManagementTemplate]:
        """
        Gets the managementTemplate property value. The managementTemplate property
        Returns: Optional[management_template.ManagementTemplate]
        """
        return self._management_template
    
    @management_template.setter
    def management_template(self,value: Optional[management_template.ManagementTemplate] = None) -> None:
        """
        Sets the managementTemplate property value. The managementTemplate property
        Args:
            value: Value to set for the managementTemplate property.
        """
        self._management_template = value
    
    @property
    def portal_link(self,) -> Optional[action_url.ActionUrl]:
        """
        Gets the portalLink property value. The portalLink property
        Returns: Optional[action_url.ActionUrl]
        """
        return self._portal_link
    
    @portal_link.setter
    def portal_link(self,value: Optional[action_url.ActionUrl] = None) -> None:
        """
        Sets the portalLink property value. The portalLink property
        Args:
            value: Value to set for the portalLink property.
        """
        self._portal_link = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def versions(self,) -> Optional[List[management_template_step_version.ManagementTemplateStepVersion]]:
        """
        Gets the versions property value. The versions property
        Returns: Optional[List[management_template_step_version.ManagementTemplateStepVersion]]
        """
        return self._versions
    
    @versions.setter
    def versions(self,value: Optional[List[management_template_step_version.ManagementTemplateStepVersion]] = None) -> None:
        """
        Sets the versions property value. The versions property
        Args:
            value: Value to set for the versions property.
        """
        self._versions = value
    

