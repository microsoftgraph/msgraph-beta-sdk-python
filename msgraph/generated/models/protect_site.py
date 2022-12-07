from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

label_action_base = lazy_import('msgraph.generated.models.label_action_base')
site_access_type = lazy_import('msgraph.generated.models.site_access_type')

class ProtectSite(label_action_base.LabelActionBase):
    @property
    def access_type(self,) -> Optional[site_access_type.SiteAccessType]:
        """
        Gets the accessType property value. The accessType property
        Returns: Optional[site_access_type.SiteAccessType]
        """
        return self._access_type
    
    @access_type.setter
    def access_type(self,value: Optional[site_access_type.SiteAccessType] = None) -> None:
        """
        Sets the accessType property value. The accessType property
        Args:
            value: Value to set for the accessType property.
        """
        self._access_type = value
    
    @property
    def conditional_access_protection_level_id(self,) -> Optional[str]:
        """
        Gets the conditionalAccessProtectionLevelId property value. The conditionalAccessProtectionLevelId property
        Returns: Optional[str]
        """
        return self._conditional_access_protection_level_id
    
    @conditional_access_protection_level_id.setter
    def conditional_access_protection_level_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conditionalAccessProtectionLevelId property value. The conditionalAccessProtectionLevelId property
        Args:
            value: Value to set for the conditionalAccessProtectionLevelId property.
        """
        self._conditional_access_protection_level_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ProtectSite and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.protectSite"
        # The accessType property
        self._access_type: Optional[site_access_type.SiteAccessType] = None
        # The conditionalAccessProtectionLevelId property
        self._conditional_access_protection_level_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectSite
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectSite()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_type": lambda n : setattr(self, 'access_type', n.get_enum_value(site_access_type.SiteAccessType)),
            "conditional_access_protection_level_id": lambda n : setattr(self, 'conditional_access_protection_level_id', n.get_str_value()),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("conditionalAccessProtectionLevelId", self.conditional_access_protection_level_id)
    

