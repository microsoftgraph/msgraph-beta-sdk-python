from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_url = lazy_import('msgraph.generated.models.action_url')
entity = lazy_import('msgraph.generated.models.entity')
management_category = lazy_import('msgraph.generated.models.managed_tenants.management_category')
management_provider = lazy_import('msgraph.generated.models.managed_tenants.management_provider')
management_template_collection = lazy_import('msgraph.generated.models.managed_tenants.management_template_collection')
management_template_step = lazy_import('msgraph.generated.models.managed_tenants.management_template_step')
template_parameter = lazy_import('msgraph.generated.models.managed_tenants.template_parameter')
workload_action = lazy_import('msgraph.generated.models.managed_tenants.workload_action')

class ManagementTemplate(entity.Entity):
    @property
    def category(self,) -> Optional[management_category.ManagementCategory]:
        """
        Gets the category property value. The management category for the management template. Possible values are: custom, devices, identity, unknownFutureValue. Required. Read-only.
        Returns: Optional[management_category.ManagementCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[management_category.ManagementCategory] = None) -> None:
        """
        Sets the category property value. The management category for the management template. Possible values are: custom, devices, identity, unknownFutureValue. Required. Read-only.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplate and sets the default values.
        """
        super().__init__()
        # The management category for the management template. Possible values are: custom, devices, identity, unknownFutureValue. Required. Read-only.
        self._category: Optional[management_category.ManagementCategory] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The description for the management template. Optional. Read-only.
        self._description: Optional[str] = None
        # The display name for the management template. Required. Read-only.
        self._display_name: Optional[str] = None
        # The informationLinks property
        self._information_links: Optional[List[action_url.ActionUrl]] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The managementTemplateCollections property
        self._management_template_collections: Optional[List[management_template_collection.ManagementTemplateCollection]] = None
        # The managementTemplateSteps property
        self._management_template_steps: Optional[List[management_template_step.ManagementTemplateStep]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of parameters used by the management template. Optional. Read-only.
        self._parameters: Optional[List[template_parameter.TemplateParameter]] = None
        # The priority property
        self._priority: Optional[int] = None
        # The provider property
        self._provider: Optional[management_provider.ManagementProvider] = None
        # The userImpact property
        self._user_impact: Optional[str] = None
        # The version property
        self._version: Optional[int] = None
        # The collection of workload actions associated with the management template. Optional. Read-only.
        self._workload_actions: Optional[List[workload_action.WorkloadAction]] = None
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the management template. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the management template. Optional. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the management template. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the management template. Required. Read-only.
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
            "category": lambda n : setattr(self, 'category', n.get_enum_value(management_category.ManagementCategory)),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "information_links": lambda n : setattr(self, 'information_links', n.get_collection_of_object_values(action_url.ActionUrl)),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "management_template_collections": lambda n : setattr(self, 'management_template_collections', n.get_collection_of_object_values(management_template_collection.ManagementTemplateCollection)),
            "management_template_steps": lambda n : setattr(self, 'management_template_steps', n.get_collection_of_object_values(management_template_step.ManagementTemplateStep)),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(template_parameter.TemplateParameter)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(management_provider.ManagementProvider)),
            "user_impact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "workload_actions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(workload_action.WorkloadAction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def information_links(self,) -> Optional[List[action_url.ActionUrl]]:
        """
        Gets the informationLinks property value. The informationLinks property
        Returns: Optional[List[action_url.ActionUrl]]
        """
        return self._information_links
    
    @information_links.setter
    def information_links(self,value: Optional[List[action_url.ActionUrl]] = None) -> None:
        """
        Sets the informationLinks property value. The informationLinks property
        Args:
            value: Value to set for the informationLinks property.
        """
        self._information_links = value
    
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
    def management_template_collections(self,) -> Optional[List[management_template_collection.ManagementTemplateCollection]]:
        """
        Gets the managementTemplateCollections property value. The managementTemplateCollections property
        Returns: Optional[List[management_template_collection.ManagementTemplateCollection]]
        """
        return self._management_template_collections
    
    @management_template_collections.setter
    def management_template_collections(self,value: Optional[List[management_template_collection.ManagementTemplateCollection]] = None) -> None:
        """
        Sets the managementTemplateCollections property value. The managementTemplateCollections property
        Args:
            value: Value to set for the managementTemplateCollections property.
        """
        self._management_template_collections = value
    
    @property
    def management_template_steps(self,) -> Optional[List[management_template_step.ManagementTemplateStep]]:
        """
        Gets the managementTemplateSteps property value. The managementTemplateSteps property
        Returns: Optional[List[management_template_step.ManagementTemplateStep]]
        """
        return self._management_template_steps
    
    @management_template_steps.setter
    def management_template_steps(self,value: Optional[List[management_template_step.ManagementTemplateStep]] = None) -> None:
        """
        Sets the managementTemplateSteps property value. The managementTemplateSteps property
        Args:
            value: Value to set for the managementTemplateSteps property.
        """
        self._management_template_steps = value
    
    @property
    def parameters(self,) -> Optional[List[template_parameter.TemplateParameter]]:
        """
        Gets the parameters property value. The collection of parameters used by the management template. Optional. Read-only.
        Returns: Optional[List[template_parameter.TemplateParameter]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[template_parameter.TemplateParameter]] = None) -> None:
        """
        Sets the parameters property value. The collection of parameters used by the management template. Optional. Read-only.
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
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
    
    @property
    def provider(self,) -> Optional[management_provider.ManagementProvider]:
        """
        Gets the provider property value. The provider property
        Returns: Optional[management_provider.ManagementProvider]
        """
        return self._provider
    
    @provider.setter
    def provider(self,value: Optional[management_provider.ManagementProvider] = None) -> None:
        """
        Sets the provider property value. The provider property
        Args:
            value: Value to set for the provider property.
        """
        self._provider = value
    
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
    
    @property
    def user_impact(self,) -> Optional[str]:
        """
        Gets the userImpact property value. The userImpact property
        Returns: Optional[str]
        """
        return self._user_impact
    
    @user_impact.setter
    def user_impact(self,value: Optional[str] = None) -> None:
        """
        Sets the userImpact property value. The userImpact property
        Args:
            value: Value to set for the userImpact property.
        """
        self._user_impact = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version property
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version property
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def workload_actions(self,) -> Optional[List[workload_action.WorkloadAction]]:
        """
        Gets the workloadActions property value. The collection of workload actions associated with the management template. Optional. Read-only.
        Returns: Optional[List[workload_action.WorkloadAction]]
        """
        return self._workload_actions
    
    @workload_actions.setter
    def workload_actions(self,value: Optional[List[workload_action.WorkloadAction]] = None) -> None:
        """
        Sets the workloadActions property value. The collection of workload actions associated with the management template. Optional. Read-only.
        Args:
            value: Value to set for the workloadActions property.
        """
        self._workload_actions = value
    

