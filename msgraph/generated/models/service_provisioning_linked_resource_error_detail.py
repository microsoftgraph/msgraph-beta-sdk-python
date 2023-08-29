from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .service_provisioning_resource_error_detail import ServiceProvisioningResourceErrorDetail

from .service_provisioning_resource_error_detail import ServiceProvisioningResourceErrorDetail

@dataclass
class ServiceProvisioningLinkedResourceErrorDetail(ServiceProvisioningResourceErrorDetail):
    # The OdataType property
    odata_type: Optional[str] = None
    # The propertyName property
    property_name: Optional[str] = None
    # The target property
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningLinkedResourceErrorDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningLinkedResourceErrorDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServiceProvisioningLinkedResourceErrorDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .service_provisioning_resource_error_detail import ServiceProvisioningResourceErrorDetail

        from .service_provisioning_resource_error_detail import ServiceProvisioningResourceErrorDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "propertyName": lambda n : setattr(self, 'property_name', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("propertyName", self.property_name)
        writer.write_str_value("target", self.target)
    

