from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
management_category = lazy_import('msgraph.generated.models.managed_tenants.management_category')
workload_action = lazy_import('msgraph.generated.models.managed_tenants.workload_action')

class ManagementAction(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
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
        Instantiates a new managementAction and sets the default values.
        """
        super().__init__()
        # The category property
        self._category: Optional[management_category.ManagementCategory] = None
        # The description for the management action. Optional. Read-only.
        self._description: Optional[str] = None
        # The display name for the management action. Optional. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The reference for the management template used to generate the management action. Required. Read-only.
        self._reference_template_id: Optional[str] = None
        # The referenceTemplateVersion property
        self._reference_template_version: Optional[int] = None
        # The collection of workload actions associated with the management action. Required. Read-only.
        self._workload_actions: Optional[List[workload_action.WorkloadAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementAction()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the management action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the management action. Optional. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the management action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the management action. Optional. Read-only.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "reference_template_id": lambda n : setattr(self, 'reference_template_id', n.get_str_value()),
            "reference_template_version": lambda n : setattr(self, 'reference_template_version', n.get_int_value()),
            "workload_actions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(workload_action.WorkloadAction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reference_template_id(self,) -> Optional[str]:
        """
        Gets the referenceTemplateId property value. The reference for the management template used to generate the management action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._reference_template_id
    
    @reference_template_id.setter
    def reference_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceTemplateId property value. The reference for the management template used to generate the management action. Required. Read-only.
        Args:
            value: Value to set for the referenceTemplateId property.
        """
        self._reference_template_id = value
    
    @property
    def reference_template_version(self,) -> Optional[int]:
        """
        Gets the referenceTemplateVersion property value. The referenceTemplateVersion property
        Returns: Optional[int]
        """
        return self._reference_template_version
    
    @reference_template_version.setter
    def reference_template_version(self,value: Optional[int] = None) -> None:
        """
        Sets the referenceTemplateVersion property value. The referenceTemplateVersion property
        Args:
            value: Value to set for the referenceTemplateVersion property.
        """
        self._reference_template_version = value
    
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("referenceTemplateId", self.reference_template_id)
        writer.write_int_value("referenceTemplateVersion", self.reference_template_version)
        writer.write_collection_of_object_values("workloadActions", self.workload_actions)
    
    @property
    def workload_actions(self,) -> Optional[List[workload_action.WorkloadAction]]:
        """
        Gets the workloadActions property value. The collection of workload actions associated with the management action. Required. Read-only.
        Returns: Optional[List[workload_action.WorkloadAction]]
        """
        return self._workload_actions
    
    @workload_actions.setter
    def workload_actions(self,value: Optional[List[workload_action.WorkloadAction]] = None) -> None:
        """
        Sets the workloadActions property value. The collection of workload actions associated with the management action. Required. Read-only.
        Args:
            value: Value to set for the workloadActions property.
        """
        self._workload_actions = value
    

