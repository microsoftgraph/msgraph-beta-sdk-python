from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import service_provisioning_error

from . import service_provisioning_error

class ServiceProvisioningXmlError(service_provisioning_error.ServiceProvisioningError):
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceProvisioningXmlError and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceProvisioningXmlError"
        # The errorDetail property
        self._error_detail: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningXmlError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningXmlError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceProvisioningXmlError()
    
    @property
    def error_detail(self,) -> Optional[str]:
        """
        Gets the errorDetail property value. The errorDetail property
        Returns: Optional[str]
        """
        return self._error_detail
    
    @error_detail.setter
    def error_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the errorDetail property value. The errorDetail property
        Args:
            value: Value to set for the error_detail property.
        """
        self._error_detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import service_provisioning_error

        fields: Dict[str, Callable[[Any], None]] = {
            "errorDetail": lambda n : setattr(self, 'error_detail', n.get_str_value()),
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
        writer.write_str_value("errorDetail", self.error_detail)
    

