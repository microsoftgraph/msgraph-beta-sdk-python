from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import service_provisioning_resource_error, service_provisioning_xml_error

@dataclass
class ServiceProvisioningError(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date and time at which the error occurred.
    created_date_time: Optional[datetime] = None
    # Indicates whether the Error has been attended to.
    is_resolved: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Qualified service instance (e.g., 'SharePoint/Dublin') that published the service error information.
    service_instance: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.serviceProvisioningResourceError":
                from . import service_provisioning_resource_error

                return service_provisioning_resource_error.ServiceProvisioningResourceError()
            if mapping_value == "#microsoft.graph.serviceProvisioningXmlError":
                from . import service_provisioning_xml_error

                return service_provisioning_xml_error.ServiceProvisioningXmlError()
        return ServiceProvisioningError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import service_provisioning_resource_error, service_provisioning_xml_error

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isResolved": lambda n : setattr(self, 'is_resolved', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceInstance": lambda n : setattr(self, 'service_instance', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isResolved", self.is_resolved)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceInstance", self.service_instance)
        writer.write_additional_data_value(self.additional_data)
    

