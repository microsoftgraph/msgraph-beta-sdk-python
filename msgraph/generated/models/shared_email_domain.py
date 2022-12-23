from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class SharedEmailDomain(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sharedEmailDomain and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The provisioningStatus property
        self._provisioning_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedEmailDomain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedEmailDomain
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedEmailDomain()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "provisioning_status": lambda n : setattr(self, 'provisioning_status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def provisioning_status(self,) -> Optional[str]:
        """
        Gets the provisioningStatus property value. The provisioningStatus property
        Returns: Optional[str]
        """
        return self._provisioning_status
    
    @provisioning_status.setter
    def provisioning_status(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningStatus property value. The provisioningStatus property
        Args:
            value: Value to set for the provisioningStatus property.
        """
        self._provisioning_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("provisioningStatus", self.provisioning_status)
    

