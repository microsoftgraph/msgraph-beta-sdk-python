from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class PronounsSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new pronounsSettings and sets the default values.
        """
        super().__init__()
        # true to enable pronouns in the organization, false otherwise. The default is false, and pronouns are disabled.
        self._is_enabled_in_organization: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PronounsSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PronounsSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PronounsSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabledInOrganization": lambda n : setattr(self, 'is_enabled_in_organization', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled_in_organization(self,) -> Optional[bool]:
        """
        Gets the isEnabledInOrganization property value. true to enable pronouns in the organization, false otherwise. The default is false, and pronouns are disabled.
        Returns: Optional[bool]
        """
        return self._is_enabled_in_organization
    
    @is_enabled_in_organization.setter
    def is_enabled_in_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledInOrganization property value. true to enable pronouns in the organization, false otherwise. The default is false, and pronouns are disabled.
        Args:
            value: Value to set for the is_enabled_in_organization property.
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
        writer.write_bool_value("isEnabledInOrganization", self.is_enabled_in_organization)
    

