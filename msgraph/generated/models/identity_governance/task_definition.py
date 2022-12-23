from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
lifecycle_task_category = lazy_import('msgraph.generated.models.identity_governance.lifecycle_task_category')
parameter = lazy_import('msgraph.generated.models.identity_governance.parameter')

class TaskDefinition(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def category(self,) -> Optional[lifecycle_task_category.LifecycleTaskCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[lifecycle_task_category.LifecycleTaskCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[lifecycle_task_category.LifecycleTaskCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new taskDefinition and sets the default values.
        """
        super().__init__()
        # The category property
        self._category: Optional[lifecycle_task_category.LifecycleTaskCategory] = None
        # The continueOnError property
        self._continue_on_error: Optional[bool] = None
        # The description of the taskDefinition.
        self._description: Optional[str] = None
        # The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parameters that must be supplied when creating a workflow task object.Supports $filter(any).
        self._parameters: Optional[List[parameter.Parameter]] = None
        # The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.
        self._version: Optional[int] = None
    
    @property
    def continue_on_error(self,) -> Optional[bool]:
        """
        Gets the continueOnError property value. The continueOnError property
        Returns: Optional[bool]
        """
        return self._continue_on_error
    
    @continue_on_error.setter
    def continue_on_error(self,value: Optional[bool] = None) -> None:
        """
        Sets the continueOnError property value. The continueOnError property
        Args:
            value: Value to set for the continueOnError property.
        """
        self._continue_on_error = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TaskDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TaskDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TaskDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the taskDefinition.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the taskDefinition.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.
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
            "category": lambda n : setattr(self, 'category', n.get_enum_value(lifecycle_task_category.LifecycleTaskCategory)),
            "continue_on_error": lambda n : setattr(self, 'continue_on_error', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(parameter.Parameter)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parameters(self,) -> Optional[List[parameter.Parameter]]:
        """
        Gets the parameters property value. The parameters that must be supplied when creating a workflow task object.Supports $filter(any).
        Returns: Optional[List[parameter.Parameter]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[parameter.Parameter]] = None) -> None:
        """
        Sets the parameters property value. The parameters that must be supplied when creating a workflow task object.Supports $filter(any).
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
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
        writer.write_bool_value("continueOnError", self.continue_on_error)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_int_value("version", self.version)
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

