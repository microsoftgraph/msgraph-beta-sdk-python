from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group = lazy_import('msgraph.generated.models.group')
policy_scope = lazy_import('msgraph.generated.models.policy_scope')

class MobilityManagementPolicy(entity.Entity):
    @property
    def applies_to(self,) -> Optional[policy_scope.PolicyScope]:
        """
        Gets the appliesTo property value. Indicates the user scope of the mobility management policy. Possible values are: none, all, selected.
        Returns: Optional[policy_scope.PolicyScope]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[policy_scope.PolicyScope] = None) -> None:
        """
        Sets the appliesTo property value. Indicates the user scope of the mobility management policy. Possible values are: none, all, selected.
        Args:
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    @property
    def compliance_url(self,) -> Optional[str]:
        """
        Gets the complianceUrl property value. Compliance URL of the mobility management application.
        Returns: Optional[str]
        """
        return self._compliance_url
    
    @compliance_url.setter
    def compliance_url(self,value: Optional[str] = None) -> None:
        """
        Sets the complianceUrl property value. Compliance URL of the mobility management application.
        Args:
            value: Value to set for the complianceUrl property.
        """
        self._compliance_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MobilityManagementPolicy and sets the default values.
        """
        super().__init__()
        # Indicates the user scope of the mobility management policy. Possible values are: none, all, selected.
        self._applies_to: Optional[policy_scope.PolicyScope] = None
        # Compliance URL of the mobility management application.
        self._compliance_url: Optional[str] = None
        # Description of the mobility management application.
        self._description: Optional[str] = None
        # Discovery URL of the mobility management application.
        self._discovery_url: Optional[str] = None
        # Display name of the mobility management application.
        self._display_name: Optional[str] = None
        # Azure AD groups under the scope of the mobility management application if appliesTo is selected
        self._included_groups: Optional[List[group.Group]] = None
        # Whether policy is valid. Invalid policies may not be updated and should be deleted.
        self._is_valid: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Terms of Use URL of the mobility management application.
        self._terms_of_use_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobilityManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobilityManagementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobilityManagementPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the mobility management application.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the mobility management application.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def discovery_url(self,) -> Optional[str]:
        """
        Gets the discoveryUrl property value. Discovery URL of the mobility management application.
        Returns: Optional[str]
        """
        return self._discovery_url
    
    @discovery_url.setter
    def discovery_url(self,value: Optional[str] = None) -> None:
        """
        Sets the discoveryUrl property value. Discovery URL of the mobility management application.
        Args:
            value: Value to set for the discoveryUrl property.
        """
        self._discovery_url = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the mobility management application.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the mobility management application.
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
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_enum_value(policy_scope.PolicyScope)),
            "compliance_url": lambda n : setattr(self, 'compliance_url', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discovery_url": lambda n : setattr(self, 'discovery_url', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "included_groups": lambda n : setattr(self, 'included_groups', n.get_collection_of_object_values(group.Group)),
            "is_valid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "terms_of_use_url": lambda n : setattr(self, 'terms_of_use_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def included_groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the includedGroups property value. Azure AD groups under the scope of the mobility management application if appliesTo is selected
        Returns: Optional[List[group.Group]]
        """
        return self._included_groups
    
    @included_groups.setter
    def included_groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the includedGroups property value. Azure AD groups under the scope of the mobility management application if appliesTo is selected
        Args:
            value: Value to set for the includedGroups property.
        """
        self._included_groups = value
    
    @property
    def is_valid(self,) -> Optional[bool]:
        """
        Gets the isValid property value. Whether policy is valid. Invalid policies may not be updated and should be deleted.
        Returns: Optional[bool]
        """
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValid property value. Whether policy is valid. Invalid policies may not be updated and should be deleted.
        Args:
            value: Value to set for the isValid property.
        """
        self._is_valid = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_str_value("complianceUrl", self.compliance_url)
        writer.write_str_value("description", self.description)
        writer.write_str_value("discoveryUrl", self.discovery_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("includedGroups", self.included_groups)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_str_value("termsOfUseUrl", self.terms_of_use_url)
    
    @property
    def terms_of_use_url(self,) -> Optional[str]:
        """
        Gets the termsOfUseUrl property value. Terms of Use URL of the mobility management application.
        Returns: Optional[str]
        """
        return self._terms_of_use_url
    
    @terms_of_use_url.setter
    def terms_of_use_url(self,value: Optional[str] = None) -> None:
        """
        Sets the termsOfUseUrl property value. Terms of Use URL of the mobility management application.
        Args:
            value: Value to set for the termsOfUseUrl property.
        """
        self._terms_of_use_url = value
    

