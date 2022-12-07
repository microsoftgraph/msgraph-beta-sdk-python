from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
unified_rbac_resource_action = lazy_import('msgraph.generated.models.unified_rbac_resource_action')

class UnifiedRbacResourceNamespace(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRbacResourceNamespace and sets the default values.
        """
        super().__init__()
        # Name of the resource namespace. Typically, the same name as the id property, such as microsoft.aad.b2c. Required. Supports $filter (eq, startsWith).
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Operations that an authorized principal are allowed to perform.
        self._resource_actions: Optional[List[unified_rbac_resource_action.UnifiedRbacResourceAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRbacResourceNamespace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacResourceNamespace
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRbacResourceNamespace()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "resource_actions": lambda n : setattr(self, 'resource_actions', n.get_collection_of_object_values(unified_rbac_resource_action.UnifiedRbacResourceAction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the resource namespace. Typically, the same name as the id property, such as microsoft.aad.b2c. Required. Supports $filter (eq, startsWith).
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the resource namespace. Typically, the same name as the id property, such as microsoft.aad.b2c. Required. Supports $filter (eq, startsWith).
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def resource_actions(self,) -> Optional[List[unified_rbac_resource_action.UnifiedRbacResourceAction]]:
        """
        Gets the resourceActions property value. Operations that an authorized principal are allowed to perform.
        Returns: Optional[List[unified_rbac_resource_action.UnifiedRbacResourceAction]]
        """
        return self._resource_actions
    
    @resource_actions.setter
    def resource_actions(self,value: Optional[List[unified_rbac_resource_action.UnifiedRbacResourceAction]] = None) -> None:
        """
        Sets the resourceActions property value. Operations that an authorized principal are allowed to perform.
        Args:
            value: Value to set for the resourceActions property.
        """
        self._resource_actions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("resourceActions", self.resource_actions)
    

