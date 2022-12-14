from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
management_template_detailed_info = lazy_import('msgraph.generated.models.managed_tenants.management_template_detailed_info')

class ManagementIntent(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managementIntent and sets the default values.
        """
        super().__init__()
        # The display name for the management intent. Optional. Read-only.
        self._display_name: Optional[str] = None
        # A flag indicating whether the management intent is global. Required. Read-only.
        self._is_global: Optional[bool] = None
        # The collection of management templates associated with the management intent. Optional. Read-only.
        self._management_templates: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementIntent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementIntent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementIntent()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the management intent. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the management intent. Optional. Read-only.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_global": lambda n : setattr(self, 'is_global', n.get_bool_value()),
            "management_templates": lambda n : setattr(self, 'management_templates', n.get_collection_of_object_values(management_template_detailed_info.ManagementTemplateDetailedInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_global(self,) -> Optional[bool]:
        """
        Gets the isGlobal property value. A flag indicating whether the management intent is global. Required. Read-only.
        Returns: Optional[bool]
        """
        return self._is_global
    
    @is_global.setter
    def is_global(self,value: Optional[bool] = None) -> None:
        """
        Sets the isGlobal property value. A flag indicating whether the management intent is global. Required. Read-only.
        Args:
            value: Value to set for the isGlobal property.
        """
        self._is_global = value
    
    @property
    def management_templates(self,) -> Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]]:
        """
        Gets the managementTemplates property value. The collection of management templates associated with the management intent. Optional. Read-only.
        Returns: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]]
        """
        return self._management_templates
    
    @management_templates.setter
    def management_templates(self,value: Optional[List[management_template_detailed_info.ManagementTemplateDetailedInfo]] = None) -> None:
        """
        Sets the managementTemplates property value. The collection of management templates associated with the management intent. Optional. Read-only.
        Args:
            value: Value to set for the managementTemplates property.
        """
        self._management_templates = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isGlobal", self.is_global)
        writer.write_collection_of_object_values("managementTemplates", self.management_templates)
    

