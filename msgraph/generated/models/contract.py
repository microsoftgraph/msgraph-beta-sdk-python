from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class Contract(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new Contract and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.contract"
        # The contractType property
        self._contract_type: Optional[str] = None
        # The customerId property
        self._customer_id: Optional[Guid] = None
        # The defaultDomainName property
        self._default_domain_name: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
    
    @property
    def contract_type(self,) -> Optional[str]:
        """
        Gets the contractType property value. The contractType property
        Returns: Optional[str]
        """
        return self._contract_type
    
    @contract_type.setter
    def contract_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contractType property value. The contractType property
        Args:
            value: Value to set for the contractType property.
        """
        self._contract_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Contract:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Contract
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Contract()
    
    @property
    def customer_id(self,) -> Optional[Guid]:
        """
        Gets the customerId property value. The customerId property
        Returns: Optional[Guid]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the customerId property value. The customerId property
        Args:
            value: Value to set for the customerId property.
        """
        self._customer_id = value
    
    @property
    def default_domain_name(self,) -> Optional[str]:
        """
        Gets the defaultDomainName property value. The defaultDomainName property
        Returns: Optional[str]
        """
        return self._default_domain_name
    
    @default_domain_name.setter
    def default_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultDomainName property value. The defaultDomainName property
        Args:
            value: Value to set for the defaultDomainName property.
        """
        self._default_domain_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
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
            "contract_type": lambda n : setattr(self, 'contract_type', n.get_str_value()),
            "customer_id": lambda n : setattr(self, 'customer_id', n.get_object_value(Guid)),
            "default_domain_name": lambda n : setattr(self, 'default_domain_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("contractType", self.contract_type)
        writer.write_object_value("customerId", self.customer_id)
        writer.write_str_value("defaultDomainName", self.default_domain_name)
        writer.write_str_value("displayName", self.display_name)
    

