from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class InsightsSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new insightsSettings and sets the default values.
        """
        super().__init__()
        # The ID of an Azure Active Directory group, of which the specified type of insights are disabled for its members. Default is empty. Optional.
        self._disabled_for_group: Optional[str] = None
        # true if the specified type of insights are enabled for the organization; false if the specified type of insights are disabled for all users without exceptions. Default is true. Optional.
        self._is_enabled_in_organization: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InsightsSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InsightsSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InsightsSettings()
    
    @property
    def disabled_for_group(self,) -> Optional[str]:
        """
        Gets the disabledForGroup property value. The ID of an Azure Active Directory group, of which the specified type of insights are disabled for its members. Default is empty. Optional.
        Returns: Optional[str]
        """
        return self._disabled_for_group
    
    @disabled_for_group.setter
    def disabled_for_group(self,value: Optional[str] = None) -> None:
        """
        Sets the disabledForGroup property value. The ID of an Azure Active Directory group, of which the specified type of insights are disabled for its members. Default is empty. Optional.
        Args:
            value: Value to set for the disabledForGroup property.
        """
        self._disabled_for_group = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "disabled_for_group": lambda n : setattr(self, 'disabled_for_group', n.get_str_value()),
            "is_enabled_in_organization": lambda n : setattr(self, 'is_enabled_in_organization', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled_in_organization(self,) -> Optional[bool]:
        """
        Gets the isEnabledInOrganization property value. true if the specified type of insights are enabled for the organization; false if the specified type of insights are disabled for all users without exceptions. Default is true. Optional.
        Returns: Optional[bool]
        """
        return self._is_enabled_in_organization
    
    @is_enabled_in_organization.setter
    def is_enabled_in_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledInOrganization property value. true if the specified type of insights are enabled for the organization; false if the specified type of insights are disabled for all users without exceptions. Default is true. Optional.
        Args:
            value: Value to set for the isEnabledInOrganization property.
        """
        self._is_enabled_in_organization = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("disabledForGroup", self.disabled_for_group)
        writer.write_bool_value("isEnabledInOrganization", self.is_enabled_in_organization)
    

