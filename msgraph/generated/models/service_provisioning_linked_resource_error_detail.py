from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import service_provisioning_resource_error_detail

from . import service_provisioning_resource_error_detail

class ServiceProvisioningLinkedResourceErrorDetail(service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceProvisioningLinkedResourceErrorDetail and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The propertyName property
        self._property_name: Optional[str] = None
        # The target property
        self._target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningLinkedResourceErrorDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningLinkedResourceErrorDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceProvisioningLinkedResourceErrorDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import service_provisioning_resource_error_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "propertyName": lambda n : setattr(self, 'property_name', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def property_name(self,) -> Optional[str]:
        """
        Gets the propertyName property value. The propertyName property
        Returns: Optional[str]
        """
        return self._property_name
    
    @property_name.setter
    def property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the propertyName property value. The propertyName property
        Args:
            value: Value to set for the property_name property.
        """
        self._property_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("propertyName", self.property_name)
        writer.write_str_value("target", self.target)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The target property
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The target property
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

