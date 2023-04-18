from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import service_provisioning_error, service_provisioning_resource_error_detail

from . import service_provisioning_error

class ServiceProvisioningResourceError(service_provisioning_error.ServiceProvisioningError):
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceProvisioningResourceError and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceProvisioningResourceError"
        # The errors property
        self._errors: Optional[List[service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningResourceError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningResourceError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceProvisioningResourceError()
    
    @property
    def errors(self,) -> Optional[List[service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail]]:
        """
        Gets the errors property value. The errors property
        Returns: Optional[List[service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail]] = None) -> None:
        """
        Sets the errors property value. The errors property
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import service_provisioning_error, service_provisioning_resource_error_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(service_provisioning_resource_error_detail.ServiceProvisioningResourceErrorDetail)),
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
        writer.write_collection_of_object_values("errors", self.errors)
    

