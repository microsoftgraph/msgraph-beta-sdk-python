from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
information_protection = lazy_import('msgraph.generated.models.security.information_protection')

class Security(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new security and sets the default values.
        """
        super().__init__()
        # The informationProtection property
        self._information_protection: Optional[information_protection.InformationProtection] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Security
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Security()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "information_protection": lambda n : setattr(self, 'information_protection', n.get_object_value(information_protection.InformationProtection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def information_protection(self,) -> Optional[information_protection.InformationProtection]:
        """
        Gets the informationProtection property value. The informationProtection property
        Returns: Optional[information_protection.InformationProtection]
        """
        return self._information_protection
    
    @information_protection.setter
    def information_protection(self,value: Optional[information_protection.InformationProtection] = None) -> None:
        """
        Sets the informationProtection property value. The informationProtection property
        Args:
            value: Value to set for the informationProtection property.
        """
        self._information_protection = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("informationProtection", self.information_protection)
    

