from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_resource = lazy_import('msgraph.generated.models.governance_resource')
governance_role_setting = lazy_import('msgraph.generated.models.governance_role_setting')

class GovernanceRoleDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new governanceRoleDefinition and sets the default values.
        """
        super().__init__()
        # The display name of the role definition.
        self._display_name: Optional[str] = None
        # The external id of the role definition.
        self._external_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. The associated resource for the role definition.
        self._resource: Optional[governance_resource.GovernanceResource] = None
        # Required. The id of the resource associated with the role definition.
        self._resource_id: Optional[str] = None
        # The associated role setting for the role definition.
        self._role_setting: Optional[governance_role_setting.GovernanceRoleSetting] = None
        # The templateId property
        self._template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceRoleDefinition()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the role definition.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the role definition.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external id of the role definition.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external id of the role definition.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(governance_resource.GovernanceResource)),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "role_setting": lambda n : setattr(self, 'role_setting', n.get_object_value(governance_role_setting.GovernanceRoleSetting)),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource(self,) -> Optional[governance_resource.GovernanceResource]:
        """
        Gets the resource property value. Read-only. The associated resource for the role definition.
        Returns: Optional[governance_resource.GovernanceResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[governance_resource.GovernanceResource] = None) -> None:
        """
        Sets the resource property value. Read-only. The associated resource for the role definition.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. Required. The id of the resource associated with the role definition.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Required. The id of the resource associated with the role definition.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def role_setting(self,) -> Optional[governance_role_setting.GovernanceRoleSetting]:
        """
        Gets the roleSetting property value. The associated role setting for the role definition.
        Returns: Optional[governance_role_setting.GovernanceRoleSetting]
        """
        return self._role_setting
    
    @role_setting.setter
    def role_setting(self,value: Optional[governance_role_setting.GovernanceRoleSetting] = None) -> None:
        """
        Sets the roleSetting property value. The associated role setting for the role definition.
        Args:
            value: Value to set for the roleSetting property.
        """
        self._role_setting = value
    
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
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleSetting", self.role_setting)
        writer.write_str_value("templateId", self.template_id)
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The templateId property
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The templateId property
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    

